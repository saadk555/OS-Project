import pandas as pd
import re
import datetime
from itertools import islice
import csv
import numpy
import itertools





    
#//by ahzam//
# read the dataset file
df = pd.read_csv('./ckd-dataset-v2.csv')

# check the top 5 rows of dataframe
df.head()

# as we can see row 0 and 1 contain garbadge values so we can delete these two rows
df.drop([0,1],axis=0,inplace=True)

# reset the index after droping row 1 and 2
df = df.reset_index(drop=True)

# again check the top 5 extries 
df.head()
#//by ahzam//

df1 = df.head()


            

