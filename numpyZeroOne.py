import numpy as np
# create a 3 row 3 col array of all zeros, data type float (default data type)
x = np.zeros((3,3))  
print(x)
print ('7===>>> ',x.shape,x.dtype.name , 'x has ', x.size, 'elements all zeros') 

x = np.ones((3,3))  # create a 3 row 3 col array of all ones
print(x)
print ('8===>>> ',x.shape,x.dtype.name , 'x has ', x.size, 'elements all ones')