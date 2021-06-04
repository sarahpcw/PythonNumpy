import numpy as np

x = np.array([20,30,40,50])
print ('1',x.sum())
 

x = np.array([[0,1,2,3],[10,11,12,13]])  # add the columns 0+1+2+3 : [10 12 14 16]
print ('2',x.sum()) 
print ('3',x.mean()) 


x = np.array([[0,1,2,3],[10,11,12,13]])  # add the columns 0+1+2+3 : [10 12 14 16]
print ('2',x.sum(axis=0))
print ('3',x.mean(axis=0))


x = np.array([[0,1,2,3],[10,11,12,13]])  # add the rows
print ('4',x.sum(axis=1) )

#
x = np.array([[0,1,2,3],[10,11,12,13]])  # cummulative sum along the row
print ('5',x.cumsum(axis=1))