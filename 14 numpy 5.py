import numpy as np

myItem = [ [0,1,2,3,4], [5,6,7,8,9], [10,11,12,13,14],[15,16,17,18,19]] #p48
print ()

x = np.arange(20).reshape(4,5)
print ('1===>>> ', x.shape,x.dtype.name,  x.size)  # dimensions of list x
print ( x)
