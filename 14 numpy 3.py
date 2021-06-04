import numpy as np

x = np.random.randn(5)  # 5 random numbers
print ( '2===>>> ',x.shape,   x.size, x)
print ('Max',np.max(x))
print ('min',np.min(x))
print ('sum',np.sum(x))
print ('mean',np.mean(x))
print ('count',np.size(x))



x = np.random.randn(4,4)  # 4x4 grid of random numbers
print ( '2===>>> ',x.shape,   x.size, type(x) , x)
print ('Max',np.max(x))
print ('min',np.min(x))
print ('sum',np.sum(x))
print ('mean',np.mean(x))
print ('size',np.size(x)) #  count how many numbers 


