import pandas as pd
import numpy as np
#getting information about a dataframe

df = pd.DataFrame(np.random.randn(3,3),index=['a','c','e'],columns = ['one','two','three'])
print(df)
df=df.reindex(['a','b','c','d','e']) 
print(df)


# these work oon np arrays / lists not dataframes

x = [1.,np.nan]
print (np.nan in x )     			#     True 
print (np.nan is float(np.nan) )		#     True 

print (np.nan in np.array(x) )		#     False  can't see the nan in a array
print (np.nan in np.array(x).tolist() )	#     False can't see the nan in a list
print ('position of the nan value', np.argwhere(np.isnan(x)))  #1 -- this method show the index of the nan
x = [[1,np.nan],[1,np.nan]]
print ('position of the nan value \n', np.argwhere(np.isnan(x)))  #1


