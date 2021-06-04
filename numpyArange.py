import numpy as np

x = np.arange(3)   # creates a list of integers
print (x)		# 
#
x = np.arange(3.0)		# creates a list of float values
print (x)

x = np.arange(1,9,1)	 # start , stop , step	  # creates a list of 3 integers 
print (x)

x = np.linspace(1,2,8)	 # start , stop , how many numbers	
print (x)


x = [ [1,2,3],[3,4,5] ]

y = np.array( [ [1,2,3],[3,4,5] ] ) 	
print(y)
print ('5a==>>> ',  y.shape,  y.dtype.name ,  'y has ', y.size, 'elements')

#
##cant mix data types of string and numbers when complex
## 2 rows 2 columns
x = np.array([[6,7],[8,9]], dtype=complex)
print ('6===>>> ',x.shape,  x.dtype.name , 'x has ', x.size, 'elements') 
#
##Re arrange  an np array  using reshape, get the shape using shape
#import numpy as np
x = np.arange(10,20,2)
print (x)		 

x = np.arange(20.).reshape(4,5)
print (x)	
print ('shape', x.shape)
print ('size', x.size)
print ('dtype', x.dtype)
##
z = np.array([[1, 2, 3, 4],
         [5, 6, 7, 8],
         [9, 10, 11, 12]])

print (z.shape)	
		# get the shape   which is #(3, 4)
import numpy as np 
b = np.arange(20).reshape(4,5) 			
print(b)
    #[[ 0  1  2  3  4]
    # [ 5  6  7  8  9]
    # [10 11 12 13 14]
    # [15 16 17 18 19]]
print('-------- b[2,3] : --', end="")
print(b[2,3])
    			#-------- b[2,3] : --13  single value
print('-------- b[0:4,1]: -- ')
print(b[0:4,1]) 	# row 0:4 i.e. downwards , col 1 only  
    			#[ 1  6 11 16]
print(b[0:4,2]) 	# row 0:4 i.e. downwards , col 2 only
    			#[ 2  7 12 17]
print('-------- b[:,1] : -- ') 
print(b[:,1])   	# all rows of column 1
    			#[ 1  6 11 16]
 
print('-------- b[1:3,:]: --') 
print(b[1:3,:])   	# row 1 to 3 excluding 3 and all columns
    				#[[ 5  6  7  8  9]
    				# [10 11 12 13 14]]
print('_____________________')

#
#
#
#
