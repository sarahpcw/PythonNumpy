# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 14:39:18 2019
@author: u
"""

import numpy as np

x = np.array( [[1,2,3],[4,5,6]] )
print (x)
print ('shape',x.shape, 'data type ' , x.dtype.name ,'x has ', x.size, 'elements')

print('-------- b[0:4,1]: -- ')
print(x[0:4,1]) 


x = [1.,np.nan]
print (np.nan in x )     			#     True 
print (np.nan is float(np.nan) )		#     True 

print (np.nan in np.array(x) )		#     False  can't see the nan in a array

print (np.nan in np.array(x).tolist() )	#     False can't see the nan in a list

print ('position of the nan value', np.argwhere(np.isnan(x)))  #1 -- this method show the index of the nan

x = [[1,np.nan]
    ,[1,np.nan]]
print ('position of the nan value \n', np.argwhere(np.isnan(x)))  