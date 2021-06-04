import numpy as np

mylist = [0,1,2,3,4,]


x = np.array(mylist)
print ('1===>>> ', x.shape,   x.size, type(x),  x) 

print (  np.random.randint(5) )
print (  np.random.randn(5)   )

x = np.random.randn(5)  # 5 random numbers
print ( '2===>>> ',x.shape,   x.size, type(x), x)
##
x = np.random.randn(2,4)  # 2 rows x 4 cols grid of random numbers
print ( '3===>>> ',x.shape,   x.size, type(x), '\n',x)
#

