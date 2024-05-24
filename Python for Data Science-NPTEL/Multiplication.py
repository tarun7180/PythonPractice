# -*- coding: utf-8 -*-
"""
Created on Fri May 24 22:25:06 2024

@author: Tarun
"""

strSampl = 'python'

strSampl *= 3

print(strSampl)

listMixed = [1,2,3,4,'tarun','j',7]

listMixed*2

listMixed[1]*=2

print(listMixed)

listMixed[5]*=2

print(listMixed)

sampleTuple = (1,2,3,3,2,1,'tj','ab')
print(sampleTuple)

sampleTuple[2:5]*2

from array import *
sampleArray = array('i',[1,2,3,4])
print(sampleArray)

sampleArray*2
