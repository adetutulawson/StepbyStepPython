#from json import load
import pandas as pd
df=pd.read_csv(r"C:\Users\Okeola Mudashiru\Documents\GitHub\MyOwnProjects\adetutulawson.github.io\pokemon_data.csv")
print(df)
 #to print just column names
print(df.columns)
print (df['Name'][0:5])

#3 To read each row
for index, row in df.iterrows():
   print (index , row['Name'])

