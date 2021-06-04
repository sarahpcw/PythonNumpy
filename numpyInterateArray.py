# -*- coding: utf-8 -*-
"""
Created on Sun Mar  8 09:45:45 2020

@author: u
"""

import numpy as np 
b = np.arange(20).reshape(4,5) 			
print(b)
    #[[ 0  1  2  3  4]
    # [ 5  6  7  8  9]
    # [10 11 12 13 14]
    # [15 16 17 18 19]]
print ( b.shape )
print ( b.shape[0] )
print ( b.shape[1] )

for i in range ( b.shape[0] ):
    print ( b[i][0] ) 
    
for i in range ( b.shape[1] ):
    print ( b[0][i] ) 
    
print( b[0] )

import json 
json_input = '{"persons": [{"name": "Brian", "city": "Seattle"}, {"name": "David", "city": "Amsterdam"} ] }'
dict = json.loads(json_input)
print ("dict")
print (dict)


print ("Keys => Values " )
for key,val in dict.items():
    print (key, "=>", val)

#Get only the keys from the dictionary
dictKeys = dict.keys()
print ("dictKeys " , dictKeys)

#Sorting the dictionary
print ("Keys, Values " )
for key, value in sorted(dict.items()):
    print (key, value)

print ("Keys => Values " )
for key,val in dict.items():
    print (key, "=>", val)
    x = val
   
print ("Keys => Values " )
for j in x:
    print (j)
import pandas as pd
df = pd.DataFrame(np.random.randn(3,3),index=['a','c','e'],columns = ['one','two','three'])
print(df)
print ( 'description ')
print ( df.describe(include='all') ) 

print ( 'description ')
print ( df.describe() ) 



#csv / excel file to data framse
import pandas as pd
import numpy as np

df = pd.read_excel('MLBPlayerSalaries.xlsx')
print(df)
df = pd.read_csv('C:\\Users\\u\\.spyder-py3\\DataD1\\MBPlayerSalaries200Sample2.csv')
#print (df)
#Writng To A Csv File
#df.sample(200).to_csv('MBPlayerSalaries200Sample22.csv')
print (df.shape)
g1 = df.groupby(["Team"]).size().reset_index(name='Number of people per team')
print('g1 \n',g1)
g1 = df.groupby(["Team"]).sum()
print('Sum \n',g1)
print ('Unique Team names' , df["Team"].unique() )
duplicated_player = df.duplicated(subset=['Player'], keep=False)
print (duplicated_player)
a = df.agg(['sum','min'])
print ( 'aggregate ' , a.shape, '\n', a.iloc[:,3:]) 
a = df.loc[:,['Team','Player','Salary']]
grouped = a.groupby('Team')  
print(grouped['Salary'].agg(np.mean))  

df2 = (df[df['Salary'] < 100000])
print('Salary < 100000 \n',df2.loc[:,['Player','Salary']])
#print("========= df.loc[ : , ['X','Y'] ] ==>")

df2 = (df[df['Salary'] < 421000].sample(frac=.99).head())
print('Salary < 421000 \n',df2.loc[:,['Player','Salary']])

df3 = df[(df['Salary'] < 421000) & (df['Year'] < 2000)].sample(frac=.1).head()
print("df['Year'] < 2000) \n" ,df3.loc[:,['Player','Salary']])


import pandas as pd
import numpy as np
df1 = pd.DataFrame({'name': ['Anastasia', 'Anastasia', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
'city': ['California', 'Los Angeles', 'California', 'California', 'California', 'Los Angeles', 'Los Angeles', 'Georgia', 'Georgia', 'Los Angeles']})
print (df1)
g1 = df1.groupby(["city"]).size().reset_index(name='Number of people')
print(g1)

#Drop duplicated rows based on a column's value
#Permalink
#columns and you want to drop all movies with duplicate titles:
print (df1[df1.apply(lambda row: row['name'].startswith('A'),axis=1)])


duplicated_titles = df1.duplicated(subset=['name'], keep="first")  
# could be first last or false
#(keeps the first row where there are duplicates, the last or none), 
print ( duplicated_titles )
# tilde is used to to dataframe subraction!
df2 = df1[~duplicated_titles]  # without the duplicated titles
print(df2)


import pandas as pd
#import numpy as np

df1 = pd.DataFrame(
        {
          'A':['A0','A1','A2'],
          'B':['B0','B1','B2'],
          'C':['C0','C1','C2']                
                }, index=[0,1,2])

df2 = pd.DataFrame(
        {
          'A':['A3','A4','A5'],
          'B':['B3','B4','B5'],
          'C':['C3','C4','C5'],
          'D':['D3','D4','D5']                
                }, index=[3,4,5])

df3 = pd.DataFrame(
        {
          'A':['A6','A7','A8'],
          'B':['B6','B7','B8'],
          'C':['C6','C7','C8'],
          'D':['D6','D7','D8']                
                }, index=[6,7,8])

frames = [df1,df2,df3]
print('Frames \n',frames)
result = pd.concat(frames)
print('Result \n', result)


import pandas as pd
import numpy as np
frame = pd.DataFrame({'name': ['Anastasia', 'Anastasia', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
'city': ['California', 'Los Angeles', 'California', 'California', 'California', 'Los Angeles', 'Los Angeles', 'Georgia', 'Georgia', 'Los Angeles'],
'Salary': [2000, 3000, 44000, 5000, 6000, 7000, 8000, 9000, 10000, 11000]})
print (frame)


print ('max', frame['Salary'].max())
print ('min', frame['Salary'].min())
print ('rank',frame['Salary'].rank())
print ('mean',frame['Salary'].mean())
print ( 'count of a in every name')
print (frame['name'].str.count('a'))# print the count of a in every name
print ( 'replace j with $')
print ( frame['name'].str.replace('J','$') )
print ("After Stripping:")
print (frame['name'].str.strip()) # removes training and leading spaces

print ( 'sum',frame['Salary'].sum())  
#Returns count of appearance of pattern in each element.
