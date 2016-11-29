'''
Created on 2016.11.20.

@author: xulei
'''
import pandas as pd
import numpy as np

df=pd.read_csv('/Users/guozhiqi-seven/VaccinesApplication/data preparation/dataset.csv',index_col=0)
#use loc instead of state because there are data for NY city, NY, NY upstate seperately
#so it causes potential duplicates( there are three state named NY so it retrieve NY three times
#also due to the system, same records will retrieve twice under certain condition
df=df.drop_duplicates()
grouped=df.groupby(['year','loc','disease']).sum()


grouped=grouped.drop('week',1)
grouped=grouped.reset_index()

#remove the data of new york city and upstate new york because it potentially clashes with new york
group_NYout=grouped[np.logical_and(grouped['loc']!='NEW YORK CITY',grouped['loc'] != 'UPSTATE NEW YORK')]

#print(group_NY_out.head())
#print(group_NY_out.shape)


