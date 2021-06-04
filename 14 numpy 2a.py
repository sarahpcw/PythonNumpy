import numpy as np

x = np.arange(0,20,1) 
print(x)

x = np.arange(20)
print ( x)

x = np.arange(24).reshape(4,6)
print (x)

print ('Max',np.max(x))
print ('min',np.min(x))
print ('sum',np.sum(x))
print ('mean',np.mean(x))


#
x = np.arange(33).reshape(11,3) 
print ('7===>>> ',x.shape, x.dtype.name , x.size)
print (x)
#
x = np.linspace(0,2,9)  #9 nummern von 0 bis 2 
x = x.reshape(3,3)
print(x)



