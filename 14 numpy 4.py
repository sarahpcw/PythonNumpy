import pandas as pd
import numpy as np
#getting information about a dataframe

df = pd.DataFrame(np.random.randn(3,3),index=['a','z','e'],columns = ['one','two','three'])
print(df)

print ( df.index.values)
print ('col', df.columns)
#
print ('Max',np.max(df.index.values))
print ('min',np.min(df.index.values))
#
x = df.loc[:,'one']
m = df.loc[:,'two']
n = df.loc[:,'three']
y = x + m
print (y)

#print('max x', np.max(x), type(x))
#print('min x', np.min(x) )
#print('mean x', np.mean(x) )
#print('sum x', np.sum(x) )
#print('size x', np.size(x) )
#
##
#print ('col', df.columns)
#for val in  ( (df.columns) ): 
#     print ( 'max of col:', val, np.max(df.loc[:,val] ) )
