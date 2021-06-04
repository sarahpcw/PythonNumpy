# -*- coding: utf-8 -*-

"""
###################################################
numpy
statistical functions - page 54
min max  median mean average stddev
the standard deviation is sqrt(mean(abs(x - x.mean()) **2))
###################################################

"""
import numpy as np
# universal functions pg 53
 
a = np.array([[1,2,3], [4,5,6], [7,8,9]])
print(a)
print('mins of every row',np.amin(a,1)) # for each row, the min value
print('the row that has the lowest values',np.amin(a,0))  
print('min of all values',np.amin(a))
#  
print('max of every col',np.amax(a,1)) # for each row, the min value
print('the row that has the highest values',np.amax(a,0)) # row 1 i.e. 4,5,6
print('max of all values',np.amax(a))

print(np.median(a))
print(np.mean(a))
print(np.average(a))

print(np.median(a,1))
print(np.mean(a,1))
print(np.average(a,1))

print(np.median(a,0))
print(np.mean(a,0))
print(np.average(a,0))

print('standard deviation',np.std([5,5,6,5]))