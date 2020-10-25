#!/usr/bin/env python
# coding: utf-8

# In[4]:


path_folder='C:/Users/emanu/Documents/Polito/Exmah/EMG_2Chs'
file1=path_folder+'/EMG-S1'
file2=path_folder+'/EMG-S2'
file3=path_folder+'/EMG-S3'

files=[file1,file2,file3]


# In[9]:


import os
from csv import reader

signals=[]
#It will be a list of tuples, (signal, label)
for file in files:
    for f in os.listdir(file):
        label=f.replace('.csv','')
        with open(file+'/'+f, 'r') as csv_file:
            signal=[]
            csv_reader = reader(csv_file)
            for line in list(csv_reader):
                signal.append(line[0])
        signals.append((signal,label))


# In[12]:




