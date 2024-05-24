# -*- coding: utf-8 -*-
"""
Created on Fri May 24 18:02:25 2024

@author: Tarun
"""

#String concatenation
strSampl = 'python'

print(strSampl+'','practice')

print(strSampl)

newString = strSampl+'','practice'

print(newString)


#List concatenation
listMixed = [1,2,3,4,'tarun','j',7]

listMixed+['python']


#Array concatenation

from array import *

sampleArray = array('i',[1,2,3,4])

sampleArray+array('i',[50,60])

#Tuple concatenation

sampleTuple = (1,2,3,4,3,'py')

sampleTuple+=('th','on')

print(sampleTuple)

#Set concatenation

sampleSet1 = {'one',1,'a'}

sampleSet1=sampleSet1,24

print(sampleSet1)
