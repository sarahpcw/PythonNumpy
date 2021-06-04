# -*- coding: utf-8 -*-

"""
###################################################
numpy
splitting - page 53
exp and sqrt
###################################################

"""
import numpy as np
# universal functions pg 52
 

# splitting page 53
a = np.floor([[9.,8.,4.,8.,8.,4.,1.,2.,6.,8.,0.,1.]
              ])
print(a)
print(np.hsplit(a,4) )
print('_____________________')
print(np.hsplit(a,4) ) # split a into 4 ( 2 rows, so 8)
a = np.floor([[9.,8.,4.,8.,8.,4.,1.,2.,6.,8.,0.,1.],
              [2.,7.,9.,9.,2.,7.,8.,1.,2.,9.,7.,5.]
              ])
print(a)
print(np.hsplit(a,4) ) # split a into 4 ( 2 rows, so 8)

print(np.hsplit(a,(2,6)) ) # split a after 2nd row and 6th col  == ???

