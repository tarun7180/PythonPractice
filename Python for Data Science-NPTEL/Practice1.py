# -*- coding: utf-8 -*-
"""
Created on Wed May 22 22:37:00 2024

@author: Tarun
"""

from array import *

strSampl = 'python'
print(strSampl)

listNumbers = [1,2,3,4,5,5,5,5]

print(listNumbers)

listMixed = [1,2,3,4,'tarun','j',7]
print(listMixed)

sampleArray = array('i',[1,2,3,4])
print(sampleArray)

for i in sampleArray : print(i)

sampleTuple = (1,2,3,3,2,1,'tj','ab')
print(sampleTuple)

sampleDict1 = {1:"one", "two":2, 3:"three", "four":4, 5:5}
print(sampleDict1)

sampleDict2 = dict([(1,'one'),('two',2),(3,'three'),('four',4),(5,5)])
print(sampleDict2)

sampleSet1 = {'one',1,'a'}
print(sampleSet1)

sampleset2 = set('tarun jain')
print(sampleset2)

rangeSample = range(2,10,2)
print(rangeSample)

for x in rangeSample : print(x)
