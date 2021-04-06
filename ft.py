import pandas as pd
import numpy as np

def feature1(df, window=200,shifting=1):
    stat_rms = 1
    stat_mav = 1
    stat_sav = 1
    stat_std = 1
    stat_hp = 1
    stat_wl = 1
    stat_zc = 0
    stat_ssc = 0
    all_stat = [stat_rms,stat_mav,stat_sav,stat_std,stat_hp,stat_zc,stat_ssc,stat_wl]
    fitur = ['rms','mav','sav','std','hp','zc','ssc','wl']
    all_data = {'class':[],}
    kolom = list(df.columns)
    kolom.remove("class")
    kolom.remove("time")
    t0 = 1
    t1 = window
    for i in range(len(all_stat)):
        if all_stat[i] == 1:
            for j in range(len(kolom)):
                if fitur[i] == "hp":
                    for k in range(3):
                        all_data[kolom[j]+" "+fitur[i]+str(k+1)] = []
                else:
                    all_data[kolom[j]+" "+fitur[i]] = []

    for i in range(df.shape[0]):
        if t1>df['time'][df.shape[0]-1]-window:
            break
        else:
            data_window = df[(df['time']>=t0) & (df['time']<=t1)].reset_index()
            data_window.drop(['index'],axis=1)
            # print(data_window['time'])
            t0 = t0 + shifting
            t1 = t1 + shifting
            kelas_max = []
            uniq = data_window['class'].unique()
            val = data_window['class'].value_counts()
            for j in uniq:
                kelas_max.append(j)
            all_data['class'].append(uniq[kelas_max.index(max(kelas_max))])
            for k in range(len(kolom)):
                if stat_rms == 1:
                    rms = np.sqrt(sum(data_window[kolom[k]]**2)/len(data_window))
                    all_data[kolom[k]+" rms"].append(rms)
                if stat_mav == 1:
                    mav = np.mean(np.abs(data_window[kolom[k]]))
                    all_data[kolom[k]+" mav"].append(mav)
                if stat_sav == 1:
                    sav = np.sum(np.abs(data_window[kolom[k]]))
                    all_data[kolom[k]+" sav"].append(sav)
                if stat_std == 1:
                    stnd = np.std(data_window[kolom[k]])
                    all_data[kolom[k]+" std"].append(stnd)
                if stat_hp == 1:
                    hp1 = np.var(data_window[kolom[k]])
                    d1 = np.diff(data_window[kolom[k]])/np.diff(data_window["time"])
                    d2 = np.diff(d1)/np.diff(data_window['time'][0:len(data_window)-1])
                    hp2 = np.sqrt(np.var(d1)/hp1)
                    hp3 = np.sqrt((np.var(d2)/np.var(d1))/hp2)
                    all_data[kolom[k]+" hp1"].append(hp1)
                    all_data[kolom[k]+" hp2"].append(hp2)
                    all_data[kolom[k]+" hp3"].append(hp3)
                if stat_wl == 1:
                    wl = 0
                    for m in range(1,len(data_window)):
                        wl = wl + abs(data_window[kolom[k]][m]-data_window[kolom[k]][m-1])
                    all_data[kolom[k]+" wl"].append(wl)
    return pd.DataFrame(all_data)

def feature(df, window=200,shifting=1):
    stat_rms = 1
    stat_mav = 0
    stat_sav = 0
    stat_std = 0
    stat_hp = 0
    stat_zc = 0
    stat_ssc = 0
    stat_wl = 0
    all_stat = [stat_rms,stat_mav,stat_sav,stat_std,stat_hp,stat_zc,stat_ssc,stat_wl]
    fitur = ['rms','mav','sav','std','hp','zc','ssc','wl']
    all_data = {'class':[],}
    kolom = list(df.columns)
    kolom.remove("class")
    kolom.remove("time")
    t0 = 1
    t1 = window
    for i in range(len(all_stat)):
        if all_stat[i] == 1:
            for j in range(len(kolom)):
                all_data[kolom[j]+" "+fitur[i]] = []

    for i in range(df.shape[0]):
        if t1>df['time'][df.shape[0]-1]-window:
            break
        else:
            data_window = df[(df['time']>=t0) & (df['time']<=t1)]
            # print(data_window['time'])
            t0 = t0 + shifting
            t1 = t1 + shifting
            kelas_max = []
            uniq = data_window['class'].unique()
            val = data_window['class'].value_counts()
            for j in uniq:
                kelas_max.append(j)
            all_data['class'].append(uniq[kelas_max.index(max(kelas_max))])
            for k in range(len(kolom)):
                if stat_rms == 1:
                    rms = np.sqrt(sum(data_window[kolom[k]]**2)/len(data_window))
                    all_data[kolom[k]+" rms"].append(rms)
                if stat_mav == 1:
                    mav = np.mean(np.abs(data_window[kolom[k]]))
                    all_data[kolom[k]+" mav"].append(mav)
                if stat_sav == 1:
                    sav = np.sum(np.abs(data_window[kolom[k]]))
                    all_data[kolom[k]+" sav"].append(sav)
                if stat_std == 1:
                    stnd = np.std(data_window[kolom[k]])
                    all_data[kolom[k]+" std"].append(stnd)
                if stat_hp == 1:
                    hp1 = np.var(data_window[k])
                    all_data[kolom[k]+" hp"].append(hp1)
    return pd.DataFrame(all_data)
