#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[8]:


myList = [1,2,3,4,5,6,7,8,9]
print(myList)


# In[9]:


#To create numpy array from python list
myArray = np.array(myList,dtype=int)
print(myArray)


# In[11]:


#Method to reshape the numpy array, it will not update the exiting numpy array, 
#it will create new numpy array with the new dimensions
newArray = myArray.reshape(3,3)
print(myArray)
print(newArray)


# In[13]:


#If we give -1 then it will reshape the array into square matrix
resultArray=myArray.reshape(3,-1)
print(resultArray)


# In[14]:


#Creating numpy array from multiple lists
sampleList1 = [1,2,3,4,5]
sampleList2 = [2,4,6,8,10]
sampleList3 = [3,6,9,12,15]
mulListArr = np.array([sampleList1,sampleList2,sampleList3])
print(mulListArr)


# In[20]:


sampleArray1 = np.array(sampleList1)
sampleArray2 = np.array(sampleList2)


# In[21]:


# Adding the corresponding elements of numpy array,matrix addition
print(np.add(sampleArray1,sampleArray2))


# In[22]:


# Subtraction the corresponding elements of numpy array,matrix subtraction
print(np.subtract(sampleArray2,sampleArray1))


# In[24]:


#Multiplication of corresponding elements of numpy array
print(np.multiply(sampleArray1,sampleArray2))


# In[25]:


#Dot product of numpy array, matrix multiplication
print(sampleArray1.dot(sampleArray2))


# In[26]:


#Divide corresponding elements of one numpy array by another array
print(np.divide(sampleArray2,sampleArray1))


# In[ ]:




