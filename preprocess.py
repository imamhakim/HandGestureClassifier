import matplotlib.pyplot as plt 
from sklearn import preprocessing as prep
import pandas as pd
import numpy as np 

def normalisasi(df):
    kolom = list(df.columns)
    kolom.remove('class')
    kolom.remove('time')
    #normalisasi data
    scaler = prep.MinMaxScaler(feature_range=(-1,1))
    # scaler = prep.StandardScaler()
    rescale = np.abs(scaler.fit_transform(df[kolom]))
    newdata = pd.DataFrame(rescale, columns=kolom)
    newdata = pd.concat([df[['time','class']],newdata],axis=1)
    return newdata

def butter_low_pass(df):
    from scipy import signal
    kolom = list(df.columns)
    kolom.remove('class')
    kolom.remove('time')
    dataFilter = {}
    for i in range(len(kolom)):
        fs = 1000 #frekuensi sampling 1 kHz
        nyqs = 0.5 * fs
        fcut = 5 #frekuensi cut off 5 Hz
        normal_fcut = fcut/nyqs
        b,a = signal.butter(4, normal_fcut, btype="low", analog=False)
        yfilter = signal.filtfilt(b,a,df[kolom[i]])
        dataFilter[kolom[i]]= yfilter.T
    return pd.concat([df[['time','class']],pd.DataFrame(dataFilter, columns = kolom)], axis=1)
    
def butter_high_pass(df):
    from scipy import signal
    kolom = list(df.columns)
    kolom.remove('class')
    kolom.remove('time')
    dataFilter = {}
    for i in range(len(kolom)):
        fs = 1000 #frekuensi sampling 1 kHz
        nyqs = 0.5 * fs
        fcut = 5 #frekuensi cut off 5 Hz
        normal_fcut = fcut/nyqs
        b,a = signal.butter(4, normal_fcut, btype="high", analog=False)
        yfilter = signal.filtfilt(b,a,df[kolom[i]])
        dataFilter[kolom[i]]= yfilter.T
    return pd.concat([df[['time','class']],pd.DataFrame(dataFilter, columns = kolom)], axis=1)