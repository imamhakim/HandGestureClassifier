import preprocess as p 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import ft

allDataset = []
for i in range (1,37):  
    print(i)
    file = "/Users/ImamHakim/Desktop/python/TUBES3/Dataset/"+str(i)+"/"+str(i)+"_2.txt"
    df = pd.read_csv(file,delimiter='\t');
    # dfFilter = p.butter_high_pass(df);
    norm = p.normalisasi(df);
    allDataset.append(ft.feature1(norm,shifting=10))

if len(allDataset)>1:
    combinedDataset = pd.concat(allDataset,ignore_index=True)
else:
    combinedDataset = allDataset[0]

combinedDataset.to_csv('test_50_50_normalisasi_nofilter_8fitur.txt', index=None, sep='\t', mode='a')
# ft.feature_extraction(dfFilter,200,2)