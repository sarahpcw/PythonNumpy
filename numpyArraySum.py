import numpy as np

#sum, min, max on single array
x = np.array([20,30,40,50])
print (x.sum() )
print (x.min()  )
print (x.max()  )
print (x.size  )
# not exist print (x.average()  )

#sum on 2d array
x = np.array([[0,1,2,3]
            ,[10,11,12,13]])  
print (x.sum(axis=0))			# [10 12 14 16] add downwards the columns  0+10=10, 1+11 = 12,14,16

x = np.array([[0,1,2,3]
            ,[10,11,12,13]])  
print (x.sum(axis=1))			# [6 46] add across the rows   0+1+2+3 = 6, 10+11+12+13=46

x = np.array([[0,1,2,3]
            ,[10,11,12,13]]) 
print (x.cumsum(axis=1))		# cummulative sum along the row

x = np.array([[0,1,2,3]
            ,[10,11,12,13]
            ,[11,12,13,14]]) 
print (x.cumsum(axis=0))		# cummulative sum along the column

x = np.array([4,16,25,36])
b = np.sqrt(x)
print(b)
x = np.array([8,27,64])
b = np.cbrt(x)
print(b)