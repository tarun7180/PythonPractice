# -*- coding: utf-8 -*-
"""
Created on Fri May 24 17:37:47 2024

@author: Tarun
"""

# String slicing
strSampl = 'python'

strSampl[slice(1,4,2)]

strSampl[:]

#List slicing

listMixed = [1,2,3,4,'tarun','j',7]

print(listMixed)

print(listMixed[:3])

print(listMixed[2:])

listMixed[2:4]


#Array slicing

from array import *

sampleArray = array('i',[1,2,3,4])

sampleArray[1:]

sampleArray[1:-1]


#Range slicing

rangeSample = range(2,10,2)

print(rangeSample[:-2])
