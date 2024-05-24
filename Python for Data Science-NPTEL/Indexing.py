# -*- coding: utf-8 -*-
"""
Created on Fri May 24 12:18:57 2024

@author: Tarun
"""

# String: Indexing
sampleString = 'leaning'

sampleString.index('l')

sampleString.index('ning')

sampleString[7]

sampleString[-2]

sampleString[-9]


#List: Indexing

sampleList = [1,2,'a','tarun',1]

sampleList.index('tarun')

sampleList[2]

sampleList[-1]


#Array: Indexing

from array import *

sampleArray = array('i',[1,2,3,4])

for x in sampleArray: print(x)

sampleArray[-3]


#Tuple: Indexing

sampleTuple = (1,2,3,4,3,'py')

sampleTuple.index('py')

sampleTuple[2]
