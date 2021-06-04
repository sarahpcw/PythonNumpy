# -*- coding: utf-8 -*-
"""
Created on Fri Sep 14 12:28:49 2018

@author: u
"""
import numpy as np
x = np.fromfunction(lambda i, j: i == j, (3, 3), dtype=int)
print(x)
#array([[ True, False, False],
#       [False,  True, False],
#       [False, False,  True]])

x = np.fromfunction(lambda i, j: i + j, (3, 3), dtype=int)
print(x)
#array([[0, 1, 2],
#       [1, 2, 3],
#       [2, 3, 4]])

#0 1 2 
#0 1 2 
#0 1 2
#
#0 1 2
#1 2 3
#2 3 4

# create a multidimensional array page 52
def f(x,y):
    return x + y*2
b = np.fromfunction(f,(4,5),dtype=int)
print(b)