from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

import config.config as c
import util.util as u
import util.dataUtil as d
import util.hmmUtil as h
import util.gmmUtil as g

import numpy as np
from sklearn.hmm import GMMHMM
from sklearn.mixture import GMM


class Plot():
    
    def __init__(self, path="data/gesture_0.txt", index=0):
        self.path = path
        self.dp = d.DataUtil()
        self.mu = h.HMM_Util()
        self.surf = None     
        self.index = index
        self.dClass = 1
        self.data = u.loadData(path)
        self.X = []
        self.Y = []
        self.Z = []


    def setData(self, data):
        self.data = data

    def trainModel(self):
        obsTrain, obsTest = self.dp.splitData(self.data)
        model, score = self.mu.buildModel(obsTrain, obsTest)
        return model, score

    def plotFigures(self, data=None):
        if data == None:
            data = self.data
        for i, d in enumerate(data):
            fig = plt.figure(i)
            self.plot(fig, d)

    def plotFigure(self, data=None, index=0):
        if data == None:
            data = self.data

        self.plot(self.fig, data[index])

    def onclick(self, event):
        if event.button == 3:
            if self.dClass == 0:
                self.name = "Data"
                p.plotData()
                self.dClass += 1
            elif self.dClass == 1:
                self.name = "RawData"
                p.plotRaw()
                self.dClass += 1
            elif self.dClass == 2:
                self.name = "GestureGMM"
                p.plotGestureGmms()
                self.dClass += 1
            elif self.dClass == 3:
                self.name = "GMM"
                p.plotGmms()
                self.dClass = 0
                

    def onscroll(self, event):
        if event.button == "down":
            self.index -= 1
        elif event.button == "up":
            self.index += 1
        
        if self.index < 0:
            self.index = len(self.data)-1
        elif self.index >= len(self.data):
            self.index = 0
        self.plot()
        #print 'button=%d, x=%d, y=%d, xdata=%f, ydata=%f'%(event.button, event.x, event.y, event.xdata, event.ydata)

    def initAxis(self):
        self.X, self.Y, self.Z = [],[],[]
        length = len(self.data[0])
        _, x, y = np.shape(self.data)
        for i in range(x):
            self.Y.append(range(0, y))
            self.X.append([i]*y) 
        self.Z = self.data[0]

    def initPlot(self, data=None):
        self.name = "Data"
        if data == None:
            data = self.data
        else:
            self.data = data
        self.fig = plt.figure()
        self.initAxis()
        self.ax = self.fig.add_subplot(111, projection='3d')
        self.surf = self.ax.plot_surface(self.X, self.Y, self.Z, rstride=1, cstride=1, cmap=cm.coolwarm, linewidth=0, antialiased=False)
        self.ax.set_zlim(-0.03, 1.03)
        self.ax.set_title(self.name + ": " + str(self.index))

        self.ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))
        
        self.fig.colorbar(self.surf, shrink=0.5, aspect=5)
        self.fig.canvas.mpl_connect('scroll_event', self.onscroll)
        self.fig.canvas.mpl_connect('button_press_event', self.onclick)



    def plot(self):
        self.ax.cla()
        self.ax = self.fig.add_subplot(111, projection='3d')
        self.surf = self.ax.plot_surface(self.X, self.Y, self.data[self.index], rstride=1, cstride=1, cmap=cm.coolwarm, linewidth=0, antialiased=False)
        self.ax.set_title(self.name + ": " + str(self.index))

        self.ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))
        self.fig.canvas.draw()

    def show(self):
        plt.show()

    def plotRaw(self):
        self.data = u.loadRaw(self.path)
        self.index = 0
        self.initAxis()
        self.plot()

    def plotGestureGmms(self):
        mg = g.GMM_Util()
        gmms = mg.sample(self.path)
        print "loading..."
        data = []
        for i in range(13):
            lis = []
            for gmm in gmms:
                sample = gmm.sample(25)
                sample = np.mean(sample, 0)
                lis.append(np.ravel(sample))
            data.append(lis)
        print np.shape(data)
        self.data = data
        self.index = 0
        self.initAxis()
        self.plot()

    def plotGmms(self):
        model, score = None, 0
        print "loading..."
        while True:
            model, score = self.trainModel()
            if model != None:
                break
        data = []
        for gmm in model.gmms_:
            data.append(gmm.sample(13))
        print np.shape(data)

        self.data = data
        self.index = 0
        self.initAxis()

        self.plot()

if __name__ == "__main__":

    p = Plot("data/gesture_0.txt")
    p.initPlot()
    p.show()