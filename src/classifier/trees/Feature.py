#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
class Feature(object):

    def __init__(self):
        pass
    
    #reihenfolge der frequenzverschiebungen
    def featureOrderOfShifts(self, gesture, maxDiff, amplitudes):
        cases = {}
        cases[0] = [['right', 'left'], ['right']]
        cases[1] = [['right','left','right','left'], ['right','left','right']]
        cases[2] = [['both', 'both'], ['both']]
        
        shifts_left = self.findShifts(gesture.bins_left_filtered, 'left')
        shifts_right = self.findShifts(gesture.bins_right_filtered, 'right')
        gesture.shifts_left = shifts_left
        gesture.shifts_right = shifts_right
        shifts = shifts_left + shifts_right
        shifts = sorted(shifts,key=lambda x: x[1])
        prev = 0
        orderList = []
        for i in range(len(shifts)):
            shift = shifts[i]
            if(i > 0):
                if(prev[0] != shift[0]):
                    diffStart = shift[1] - prev[1]
                    diffStop = shift[2] - prev[2]
                    if(diffStart < maxDiff and diffStop < maxDiff):
                        orderList.pop()
                        orderList.append('both')
                    else:
                        orderList.append(shift[0])
                        prev = shift
                else:
                    orderList.append(shift[0])
                    prev = shift
                        
            else:
                orderList.append(shift[0])        
                prev = shifts[i]
        #Cases = self.findShiftCases(orderList, 0, Cases)
        #return Cases
        gesture.shift_order = orderList
        for k,v in cases.iteritems():
            if(orderList in v):
                return k   
        return "no case available", orderList
        # Herausfinden, welche Kombinationen auch noch oft vorkommen pro case oder rauswerfen?
           
    def featureAmplitudes(self, gesture):
        ampl_val = 0
        shift_order = gesture.shift_order
        if(len(shift_order) > 1):
            if(len(shift_order) == 2 and shift_order[0] != shift_order[1]):
                if(shift_order[0] == 'right'):
                    # start, stop 
                    print "SHIFTs_RIGHT", gesture.shifts_right[0]
                    maxAmpl1 = self.getMaxAmplitude(gesture.shifts_right[0][1], gesture.shifts_right[0][2], gesture.amplitudes_right_filtered)
                    maxAmpl2 = self.getMaxAmplitude(gesture.shifts_left[0][1], gesture.shifts_left[0][2], gesture.amplitudes_left_filtered)
                    #diff = abs(maxAmpl1 - maxAmpl2)
                    #print "diff", diff
                    
    def getMaxAmplitude(self, start, stop, amplitudes):
        #print amplitudes[start:stop+1]
        #print "max", max(amplitudes[start:(stop+1)])      
        #return max(amplitudes[start:(stop+1)])
        pass           
   
    #anzahl verschiebungen
    def featureCountOfShifts(self, gesture):
        countOfShiftLeft = len(self.findShifts(gesture.bins_left_filtered, 'left'))
        countOfShiftRight = len(self.findShifts(gesture.bins_right_filtered, 'right'))
        return (countOfShiftRight, countOfShiftLeft)
  
    def findShiftCases(self, orderList, dataClass, Cases):
        #cases = {}
   
        Cases[','.join(orderList)] = Cases.get(','.join(orderList), 0) + 1
        return Cases
  
    # Verschiebung ist charakterisiert durch Anfang, Ende, maximale Binanzahl 
    # und ob sie links oder rechts des Peaks ist        
    def findShifts(self, values, direction):
        commonValue = np.argmax(np.bincount(values))
        found = False
        tempStart = 0
        tempStop = 0
        tempMax = 0
        shifts = []
        for i in range(len(values)):
            value = values[i]
            if(value > commonValue and found == False):
                tempStart = i
                tempMax = values[i]
                found = True
            elif(value > commonValue and found == True):
                if(value > tempMax):
                    tempMax = values[i]
            elif(value <= commonValue and found == True):
                tempStop = i
                shift = (direction, tempStart, tempStop, tempMax)
                shifts.append(shift)
                tempStart, tempStop, tempMax = 0,0,0
                found = False
        return shifts
    
    
    