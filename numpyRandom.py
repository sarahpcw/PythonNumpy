import pandas as pd
import numpy as np
print ('\n')
print (np.random.randn(4,4))  # 4 x 4 random numbers in a 2d array
print ('\n')
print (np.random.randn(10))   # 1d list of 10 random numbers 
print ('\n')





import time
print("time", time.time())

#Datetime functions

from datetime import datetime

presentime=datetime.now() 


print(" NOW THE TIME IS:",presentime)

print("Todays Date is:",presentime.strftime('%Y-%m-%d'))

print("Year is:",presentime.year)

print("MOnth is:",presentime.month)

print("Day is:",presentime.day)

print("-------------------")


dates = pd.date_range(presentime.strftime('%Y-%m-%d'),periods=4) 
for date in dates:
     print(date)

dates = pd.date_range(presentime.strftime('%Y-%m-%d'),periods=7) 

for date in dates:
     print(date)