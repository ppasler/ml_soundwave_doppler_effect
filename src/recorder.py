import matplotlib
from numpy.lib.utils import deprecate
matplotlib.use('TkAgg')  # <-- THIS MAKES IT FAST!
import numpy as np
import pyaudio
from threading import Timer, Thread
import time

#bob
import classifier.k_means.kMeans_Helper as kmHelper
#bob end

class SwhRecorder:
    """Simple, cross-platform class to record from the microphone."""

    def __init__(self, gestureFileIO, audioConfig, recordConfig):
        """minimal garb is executed when class is loaded."""
        self.gestureFileIO = gestureFileIO
        self.frequency = float(audioConfig['frequency'])
        self.framerate = int(audioConfig['framerate'])
        self.buffersize = int(audioConfig['buffersize'])
        self.secToRecord = float(recordConfig['sectorecord'])
        self.recordingFrames = int(recordConfig['recordingframes'])
        self.recordIntervall = float(recordConfig['recordintervall'])
#         self.timerStop = False
        # frequency range (+ / -)
        frequencyToIndex = self.buffersize / (self.framerate + 0.0)
        self.leftBorder = (frequencyToIndex * self.frequency) - float(recordConfig['leftborder'])
        self.rightBorder = (frequencyToIndex * self.frequency) + float(recordConfig['rightborder'])
        self.transformedData = None
        self.initRecording()
        self.waitToFinishCurrentRecord = False
        self.setupFinish = False

        self.threadNum = 0
        self.thread = None
#         self.setup()

        self.classifyFlag = False
        self.classifier = None


        #bob
        self.kmH = kmHelper.kMeansHepler()
        self.kmeans = None
        self.checkOnline = False
        self.startBuffern = False
        
        #new
        
        self.percentRatio = 0.0
        self.gestureIdx = 0
        self.gestureArray = []
        #bob end

    def setup(self):
        """initialize sound card."""
        # TODO - windows detection vs. alsa or something for linux
        # TODO - try/except for sound card selection/initiation
        self.buffersToRecord = int(self.framerate * self.secToRecord / self.buffersize)
        if self.buffersToRecord == 0:
            self.buffersToRecord = 1
        self.samplesToRecord = int(self.buffersize * self.buffersToRecord)
        self.chunksToRecord = int(self.samplesToRecord / self.buffersize)
        self.secPerPoint = 1.0 / self.framerate

        self.audioDev = pyaudio.PyAudio()
        self.audioInStream = self.audioDev.open(format=pyaudio.paInt16, channels=1, rate=self.framerate, input=True, frames_per_buffer=self.buffersize)

        self.xsBuffer = np.arange(self.buffersize) * self.secPerPoint
        self.xs = np.arange(self.chunksToRecord * self.buffersize) * self.secPerPoint
        self.audio = np.empty((self.chunksToRecord * self.buffersize), dtype=np.int16)
        self.timerStop = False

        self.setupFinish = True

    def close(self):
        self.stopRecording()
        """cleanly back out and release sound card."""
        if(self.setupFinish and not self.waitToFinishCurrentRecord):
            self.audioInStream.stop_stream()
            self.audioInStream.close()
            self.audioDev.terminate()

    ### RECORDING AUDIO ###
    def getAudio(self):
        """get a single buffer size worth of audio."""
        audioString = self.audioInStream.read(self.buffersize)
        return np.fromstring(audioString, dtype=np.int16)

    def record(self):
        """record secToRecord seconds of audio."""
        if self.timerStop:
            return
        self.waitToFinishCurrentRecord = True
        for i in range(self.chunksToRecord):
            self.audio[i * self.buffersize:(i + 1) * self.buffersize] = self.getAudio()
        self.fft()
        if(self.classifyFlag):
            self.classify()
        elif(self.recordClass is not None):
            self.recordCount -= 1
            self.recordData.append(self.transformedData[1])
            if(self.recordCount == 0):
                self.writeGesture()
                self.initRecording()
        self.waitToFinishCurrentRecord = False
        if(not self.timerStop):
            self.t = Timer(self.recordIntervall, self.startNewThread).start()
        else:
            self.close()


    def classifyStart(self, classifier):
        self.classifier = classifier
        self.classifyFlag = True

    def classifyStop(self):
        print("classify stopped called")
        self.classifier = None
        self.classifyFlag = False

    def classify(self):
        self.classifier.classify(self.transformedData[1])

    def startNewThread(self):
        self.thread = Thread(name="Recorder-" + str(self.threadNum), target=self.record, args=())
        self.thread.start()
        self.threadNum += 1
        return self.thread

    def is_alive(self):
        if self.thread is not None:
            return self.thread.is_alive()
        return False

    def writeGesture(self):
        self.gestureFileIO.writeGesture(self.recordClass, self.recordData)
        self.callback(self.recordClass)

    def initRecording(self):
        self.recordClass = None
        self.recordCount = self.recordingFrames
        self.recordData = []
        self.callback = None

    def stopRecording(self):
        self.timerStop = True

    def setRecordClass(self, recordClass, callback):
        self.recordClass = recordClass
        self.callback = callback

    @deprecate
    def continuousStart(self):
        """CALL THIS to start running forever."""
        self.t = Thread(name="Recorder", target=self.record)
        self.t.start()

    @deprecate
    def continuousEnd(self):
        """shut down continuous recording."""
        self.timerStop = True

    ### MATH ###

    def downsample(self, data, mult):
        """Given 1D data, return the binned average."""
        overhang = len(data) % mult
        if overhang:
            data = data[:-overhang]
        data = np.reshape(data, (len(data) / mult, mult))
        data = np.average(data, 1)
        return data

    def fft(self, data=None, trimBy=1, logScale=False, divBy=4000):
        # print("fft " + str(time.time()))
        data = self.audio.flatten()
        left, right = np.split(np.abs(np.fft.fft(data)), 2)
        ys = np.add(left, right[::-1])
        ys = ys[int(self.leftBorder):int(self.rightBorder)]
        if logScale:
            ys = np.multiply(20, np.log10(ys))
        xs = np.arange(self.buffersize / 2, dtype=float)
        xs = xs[int(self.leftBorder):int(self.rightBorder)]
        if trimBy:
            i = int((self.buffersize / 2) / trimBy)
            ys = ys[:i]
            xs = xs[:i] * self.framerate / self.buffersize
        if divBy:
            ys = ys / float(divBy)
        """ frequency to index-> frequency * buffersize / framerate """
        self.transformedData = xs, ys

        #bob
        if self.startBuffern:  
            data = self.transformedData[1]
            self.bufferArray = np.roll(self.bufferArray, -1, axis=0)
            self.bufferArray[15] = self.kmH.normalizeSignalLevelSecond(data)
            if self.checkOnline:
                #maxV = np.amax(self.bufferArray[0])
                if True:#(np.sum(self.bufferArray[0] > maxV * 0.15)) - 1 > 6:
                    #print self.bufferArray.reshape(32*(self.idxRight -self.idxLeft),).shape
                    result = []
                    '''
                    outBoolArray =  self.kmH.segmentInputData(self.bufferArray, 16, .15, 6, normalize=True)
                    if outBoolArray is not None:
                        #print outBoolArray.shape
                        result = self.kmH.reduceDimensionality(outBoolArray, 16, twice=True, thrice=True)
                        if result is not None:
                            #print result.shape
                            result = np.asarray(result)
                            result = result.reshape(result.shape[0]*result.shape[1])
                            result = np.asarray(result)
                            #self.learnArray.append(result)
                            #self.learnArrayKMeans.append(result)
                    else:
                        print 'array empty !!!'                    
                    '''
                    #tmp = self.bufferArray[0:16]
                    #print 'tmp.shape ', tmp.shape
                    result = self.kmH.reduceDimensionality(self.bufferArray)
                    #print 'result : \n', self.bufferArray[0] 
                    if result is not None:
                            #print result.shape
                            result = np.asarray(result)
                            result = result.reshape(result.shape[0]*result.shape[1])
                            #result = np.asarray(result)
                    
                    if len(result) == self.kmeans.cluster_centers_.shape[1]:
                        #print result, ' , '
                        self.kMeansOnline(result)
                    else:
                        print 'len(result) : ', len(result)
        #bob end
        
    def getTransformedData(self):
        # print("get " + str(time.time()))
        return self.transformedData

    #bob
    def fillBuffer(self, bufferSize, callback):
        self.idx = 0
        self.progress = 0.0
        self.bufferSize = bufferSize
        #self.bufferArray = np.zeros((self.bufferSize, self.idxRight -self.idxLeft))
        self.bufferArray = np.zeros((self.bufferSize, 64))
        self.startBuffern = True
        self.callback = callback
        print 'fillBuffer'
        print self.bufferArray.shape
        
    def getBuffer(self):
        return self.bufferArray
    # changed scope
    def setKMeans(self, kMeans):
        self.kmeans = kMeans
        self.gestureArray = np.array(['bob\n', 'bob\n', 'bob\n', 'bob\n', 'bob\n', 'bob\n', 'bob\n', 'bob\n', 'bob\n', 'bob\n'])
        
        
        
    def kMeansOnline(self, checkArray):
        class_  = self.kmeans.transform(checkArray)
        cluster =  self.kmH.checkClusterDistance(class_, self.percentRatio)
        self.setGestureArray(cluster)
       
        if cluster == -1:
            print '-1'
        elif cluster == 0:
            print '    0'
        elif cluster == 1:
            print '        1'
        elif cluster == 2:
            print '            2'
        elif cluster == 3:
            print '                3'
        elif cluster == 4:
            print '                    4'
        elif cluster == 5:
            print '                        5'
        elif cluster == 6:
            print '                            6'
        elif cluster == 7:
            print '                                7'                                                
        
    def setGestureArray(self, cluster):
        self.gestureIdx = self.gestureIdx+1 
        class_ = "-"
        if cluster == -1:
            class_ = '\t-1\n'
        elif cluster == 0:
            class_ = '\t\t0\n'
        elif cluster == 1:
            class_ = '\t\t\t1\n'
        elif cluster == 2:
            class_ = '\t\t\t\t2\n'
        elif cluster == 3:
            class_ = '\t\t\t\t\t3\n'
        elif cluster == 4:
            class_ = '\t\t\t\t\t\t4\n'
        elif cluster == 5:
            class_ = '\t\t\t\t\t\t\t5\n'
        elif cluster == 6:
            class_ = '\t\t\t\t\t\t\t\t6\n'
        elif cluster == 7:
            class_ = '\t\t\t\t\t\t\t\t7\n'
   
        
        self.gestureArray[self.gestureIdx] = class_
        self.gestureIdx = (self.gestureIdx+1)%9                                           
    
    
    def getGestureArray(self):
        return np.asarray(self.gestureArray)
    
        
    def checkKMeansOnline(self):
        self.checkOnline = not self.checkOnline
    #new
    def setPercentRatio(self, pRatio):
        self.percentRatio = pRatio    
    #bob end
