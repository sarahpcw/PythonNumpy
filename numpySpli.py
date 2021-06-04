# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 16:10:21 2019

@author: u
"""
import numpy as np

a = np.arange(12)
print(a)
b = np.split(a,4)
for i in range (4):
    print ('row' , i , b[i])

a = np.array([[1,2,3,4,5,6],[11,12,13,14,15,16]])
b = np.hsplit(a,2)
print(b)

a = np.array([[1,2,3,4,5,6],[11,12,13,14,15,16]])
b = np.hsplit(a,3)
print(b)

a = np.array([[1,2,3,4,5,6,7,8,9],[11,12,13,14,15,16,17,18,19]])
b = np.hsplit(a,3)
print(b)
