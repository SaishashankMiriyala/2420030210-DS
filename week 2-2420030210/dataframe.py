"""import pandas as pd
data = { 'apples':[3, 2, 0, 1] , 'oranges':[0, 3, 7, 2] }
df=pd.DataFrame(data)
print(df)"""

#for index changig
"""import pandas as pd
data = { 'apples':[3, 2, 0, 1] , 'oranges':[0, 3, 7, 2] }
df=pd.DataFrame(data, index=['Ahmad', 'Ali', 'Sai', 'Shasi'])
print(df)"""

#to specify location
"""import pandas as pd
data = { 'apples':[3, 2, 0, 1] , 'oranges':[0, 3, 7, 2] }
df=pd.DataFrame(data, index=['Ahmad', 'Ali', 'Sai', 'Shasi'])
print(df.loc['Sai'])"""

#reading csv file
"""import pandas as pd
df=pd.read_csv('Iris.csv')
print(df)"""

#reading few rows
"""import pandas as pd
df=pd.read_csv('Iris.csv')
print(df.head(2))"""

#reading down rows
"""import pandas as pd
df=pd.read_csv('Iris.csv')
print(df.tail(2))"""

#details of rows and columns
"""import pandas as pd
df=pd.read_csv('Iris.csv')
print(df.info())"""

#total no.of rows and coloumns
"""import pandas as pd
df=pd.read_csv('Iris.csv')
print(df.shape)"""

#reading json files
"""import pandas as pd
df = pd.read_json("sample1.json")
print(df)"""

#how to handle the duplicates
"""import pandas as pd
df = pd.read_csv("Iris.csv")
dup_df = pd.concat([df,df])
print(df.shape)
print(dup_df.shape)"""

#drop the duplicates
"""import pandas as pd
df = pd.read_csv("Iris.csv")
dup_df = pd.concat([df,df])
dup_df.drop_duplicates(inplace=True)
print(dup_df.shape)"""

#handling duplicates
"""import pandas as pd
df = pd.read_csv("Iris.csv")
dup_df = pd.concat([df,df])
print(df.describe())"""

#more examples 
"""import pandas as pd
data=[1,2,3,10,20,30]
df=pd.DataFrame(data)
print(df)"""

#for names
"""import pandas as pd
data = {
    'Name': ['AA', 'BB'], 'Age': [30, 45]}
df = pd.DataFrame(data)
df.to_csv("App.csv", index=True)"""

#for pandas orient keyword for columns
"""import pandas as pd
data = {'col_1' :[3, 2, 1, 6], 'col_2':['a','b','c','d']}
df=pd.DataFrame.from_dict(data)
print(df)"""

#for rows with index
import pandas as pd
data = {'row_1' :[3, 2, 1, 6], 'row_2':['a','b','c','d']}
df=pd.DataFrame.from_dict(data,orient = 'index')
print(df)

"""import pandas as pd
data = { 'apples':[3, 2, 0, 1] , 'oranges':[0, 3, 7, 2] }
df=pd.DataFrame(data)
print(df)"""

#for index changig
"""import pandas as pd
data = { 'apples':[3, 2, 0, 1] , 'oranges':[0, 3, 7, 2] }
df=pd.DataFrame(data, index=['Ahmad', 'Ali', 'Sai', 'Shasi'])
print(df)"""

#to specify location
"""import pandas as pd
data = { 'apples':[3, 2, 0, 1] , 'oranges':[0, 3, 7, 2] }
df=pd.DataFrame(data, index=['Ahmad', 'Ali', 'Sai', 'Shasi'])
print(df.loc['Sai'])"""

#reading csv file
"""import pandas as pd
df=pd.read_csv('Iris.csv')
print(df)"""

#reading few rows
"""import pandas as pd
df=pd.read_csv('Iris.csv')
print(df.head(2))"""

#reading down rows
"""import pandas as pd
df=pd.read_csv('Iris.csv')
print(df.tail(2))"""

#details of rows and columns
"""import pandas as pd
df=pd.read_csv('Iris.csv')
print(df.info())"""

#total no.of rows and coloumns
"""import pandas as pd
df=pd.read_csv('Iris.csv')
print(df.shape)"""

#reading json files
"""import pandas as pd
df = pd.read_json("sample1.json")
print(df)"""

#how to handle the duplicates
"""import pandas as pd
df = pd.read_csv("Iris.csv")
dup_df = pd.concat([df,df])
print(df.shape)
print(dup_df.shape)"""

#drop the duplicates
"""import pandas as pd
df = pd.read_csv("Iris.csv")
dup_df = pd.concat([df,df])
dup_df.drop_duplicates(inplace=True)
print(dup_df.shape)"""

#handling duplicates
"""import pandas as pd
df = pd.read_csv("Iris.csv")
dup_df = pd.concat([df,df])
print(df.describe())"""

#more examples 
"""import pandas as pd
data=[1,2,3,10,20,30]
df=pd.DataFrame(data)
print(df)"""

#for names
"""import pandas as pd
data = {
    'Name': ['AA', 'BB'], 'Age': [30, 45]}
df = pd.DataFrame(data)
df.to_csv("App.csv", index=True)"""

#for pandas orient keyword for columns
"""import pandas as pd
data = {'col_1' :[3, 2, 1, 6], 'col_2':['a','b','c','d']}
df=pd.DataFrame.from_dict(data)
print(df)"""

#for rows with index
"""import pandas as pd
data = {'row_1' :[3, 2, 1, 6], 'row_2':['a','b','c','d']}
df=pd.DataFrame.from_dict(data,orient = 'index')
print(df)"""

#Data frame using student roll no ,student name,age,sec,three different subject marks and 10 rows for printing this values and after printing convert to csv file
"""import pandas as pd
data = {
    "Roll No": [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    "Student Name": ["Rahul", "Priya", "Kiran", "Anjali", "Ravi","Sneha", "Arjun", "Meena", "Varun", "Pooja"],
    "Age": [20, 21, 20, 19, 22, 20, 21, 19, 22, 20],
    "Section": ["A", "A", "B", "B", "A", "C", "C", "B", "A", "C"],
    "QC": [85, 90, 78, 88, 92, 75, 80, 95, 89, 84],
    "DS": [88, 91, 82, 85, 94, 79, 83, 90, 87, 86],
    "TOC": [80, 87, 76, 90, 89, 81, 84, 88, 85, 82]
}
df = pd.DataFrame(data)
print("Student Table:")
print(df)
df.to_csv("students.csv", index=True)
print(df.shape)
print(df.head())
print(df.head(3))
print(df.tail())
print(df.tail(2))
print(df.describe())
dup_df = pd.concat([df,df])
print(df.shape)"""

#for movies csv file
import pandas as pd
df=pd.read_csv('movies.csv')
print(df)
print(df.shape)
print(df.head())
print(df.head(3))
print(df.tail())
print(df.tail(2))
print(df.columns)
df.info()
