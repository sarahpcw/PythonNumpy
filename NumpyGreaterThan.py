import numpy as np
x1 = np.array([[1,2,3],[1,4,5]])
x2 = np.array([[13,23,33],[14,44,54]])
#Comparison functions¶
c= np.greater(x1,x2)
print("greater    ====c> \n",c)      #Return the truth value of (x1 > x2) element-wise.

c= np.greater_equal(x1,x2)
print("greater equal==c> \n",c)      #Return the truth value of (x1 >= x2) element-wise.

c= np.less(x1,x2)
print("less         ==c> \n",c)      #Return the truth value of (x1 < x2) element-wise.

c= np.less_equal(x1,x2)
print("less and equal=c> \n",c)      #Return the truth value of (x1 =< x2) element-wise.

c= np.not_equal(x1,x2)
print("not equal   ===c> \n", c)     #Return (x1 != x2) element-wise.

c= np.equal(x1,x2)
print("print a , x1 and x2 > \n",c)

