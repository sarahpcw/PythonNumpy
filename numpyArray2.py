import numpy as np

x = np.array([0.0,1.,2,3,4.56], dtype=int)  # 1 row with 5 elements
print (x)
print ('3===>>> ',x.shape, x.dtype , 'x has ', x.size, 'elements') 


x = np.array( [(1,2,3),(4,5,6)] )	#2 d array 2 rows 3 columns
print (x)
print ('shape',x.shape, 'data type ' , x.dtype.name ,'x has ', x.size, 'elements')


x = np.array( [[1,2,3],[4,5,6]] )
print (x)
print ('shape',x.shape, 'data type ' , x.dtype.name ,'x has ', x.size, 'elements')

x = np.array([0.0,1.,2,3,4.56])  # 1 row with 5 elements
print (x)
print ('3===>>> ',x.shape,x.dtype.name , 'x has ', x.size, 'elements') 

x = np.array([0.23,1.23,2.34,3.12,4.23]) 	#cant mix data types # 1 row with 5 elements
print ('4===>>> ',x.shape,x.dtype.name , 'x has ', x.size, 'elements') 

x = np.array( [ (1,2,3),(3,4,5) ] ) 		#2 d array 2 rows 3 columns
print (x)
print ('5===>>> ',x.shape,x.dtype.name ,'x has ', x.size, 'elements')

x = np.array([[6,7],[8,9]],dtype=complex) #cant mix data types 2 rows 2 columns
print ('6===>>> ',x.shape,x.dtype.name , 'x has ', x.size, 'elements') 


