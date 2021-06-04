import numpy as np

#
##sum on 2d array
x = np.array([[0,1,2,3]
            ,[10,11,12,13]])

x1 = np.array([20,30,-40,50])
x2 = np.array([20,30,40,50])
print(np.negative(x1 ))
print(np.positive(x1))
print(np.absolute(x1))
print(np.sign(x1))
#
x1 = np.array([1,2,3])
x2 = np.array([2,2,2])
print(np.power(x1, x2))
#
x1 = np.array([1.65,1.35])
print('Round to the nearest',np.rint(x1))
print('Round down',np.floor(x1))
print('Round up',np.ceil(x1))
print('Truncate',np.trunc(x1))
#
x1 = np.array([1,2,3])
x2 = np.array([15,18,2])
print('fmax',np.fmax(x1, x2))
print('fmin',np.fmin(x1, x2))
#
#print('amax',np.amax(x1, 0))
#print('amin',np.amin(x1, 0))

x1 = np.array([[1,2,3]
              ,[1,4,5]])

x2 = np.array([[13,23,33],[14,44,54]])

print('fmax',np.fmax(x1, x2))
print('fmin',np.fmin(x1, x2))

print('amax',np.amax(x1, 0))
print('amax',np.amax(x1, 1))

print('amin',np.amin(x1, 0))
print('amin',np.amin(x1, 1))




