import pandas as pd
from glob import glob

files=sorted(glob(r"C:\Users\Okeola Mudashiru\Documents\GitHub\MyOwnProjects\StepbyStepPython\Pandas-Data-Science-Tasks-master\SalesAnalysis\Sales_Data\sales*.csv"))
#print(files)

mergedata= pd.concat(
    pd.read_csv(datafile).assign(sourcefilename=datafile)
   for  datafile in files
)

mergedata.to_csv(r"C:\Users\Okeola Mudashiru\Documents\GitHub\MyOwnProjects\StepbyStepPython\Pandas-Data-Science-Tasks-master\SalesAnalysis\Sales_Data\salesMaster.csv")

#def new_func():
pd.read_csv(r"C:\Users\Okeola Mudashiru\Documents\GitHub\MyOwnProjects\StepbyStepPython\Pandas-Data-Science-Tasks-master\SalesAnalysis\Sales_Data\salesMaster.csv")

#master=new_func()
#print(master)

#nan_values = mergedata[mergedata.isna().any(axis=1)]
#nan_values.head(5)