from importlib.metadata import files
import pandas as pd
import glob
import os


####Printing out information of a single csv file

#df=pd.read_csv(r"C:\Users\Okeola Mudashiru\Documents\GitHub\MyOwnProjects\StepbyStepPython\Pandas-Data-Science-Tasks-master\SalesAnalysis\Sales_Data\Sales_April_2019.csv")
#print(df)
#df.head()

files=[file for file in os.listdir(r"C:\Users\Okeola Mudashiru\Documents\GitHub\MyOwnProjects\StepbyStepPython\Pandas-Data-Science-Tasks-master\SalesAnalysis\Sales_Data")]
for file in files:
   #print (file)

### setting the path for joining multiple files
    files=os.path.join(r"C:\Users\Okeola Mudashiru\Documents\GitHub\MyOwnProjects\StepbyStepPython\Pandas-Data-Science-Tasks-master\SalesAnalysis\Sales_Data", "sales*.csv")

# list of merged files returned
files = glob.glob(files)
#print (files)
####Merging 12months of data into a single file
df = pd.concat(
   map(pd.read_csv, files), ignore_index=True)
print(df)

