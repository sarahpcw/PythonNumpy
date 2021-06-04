import numpy as np
# Addition - add 2 arrays
x = np.array([20,30,40,50]) 		
y = np.array([20,30,40,50])
c = x + y					#add columnwise
print (c)  				    #[ 40  60  80 100]

# Addition - add 2 arrays
x = np.array([20,30,40,50]) 		
y = np.array([20,30,40,50])
c = x - y					#add columnwise
print (c)  

x = np.array([[1,1],[0,1]]) 		# add element wise  
y = np.array([[2,0],[3,4]])
c = x + y
print (c) 	
# [[3 1]  add the row 1's 
# [3 5]]  then add the row 2's

# multiply arrays
x = np.array([20,30,40,50]) 		
y = np.array([20,30,40,50])
print ( x * y)				#multiply columnwise 	#[ 400  900 1600 2500]		

x = np.array([[1,1],[0,1]]) 		# product element wise page 51
y = np.array([[2,0],[3,4]])
print ( x * y )				
#[[2 0]
# [0 4]]

x = np.array([20,30,40,50]) 		
y = np.array([20,30,40,50])
c = x / y					#add columnwise
print (c) 
