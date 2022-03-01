import pandas as pd
import matplotlib.pyplot as plt


def LRF_calc(df,bm):
    '''Function to calculate a Linear Response Function from 
    Levermann et al. (2020) based on stats output from BISICLES
    df: dataframe containing BISICLES data
    returns dataframe with additional columns'''
    
    sea_area = 361.8
    rho_i = 0.917
    
    #df['vafdiff'] = df.volumeAbove - df.volumeAbove.iloc[0]
    df['ice_mass'] = (df.volumeAbove/(10**9)) * rho_i
    df['SLE'] = df.ice_mass*(1/sea_area)
    df['SLEm'] = -(df.SLE)/1000
    df['difference'] = df.SLEm.diff()
    #df['difforig'] = df.difference - df.difference.iloc[1]
    #df['LRF'] = df.difforig/bm
    df['LRF'] = df.difference/bm
    df['SMA10'] = df.LRF.rolling(10).mean()
    return df

def LRF_ts(df,key,plot_path):
    '''Function to plot LRF from Levermann et al. (2020) based on
    dataframe created in LRF_calc. Returns a plot with LRF and
    10 year running mean'''
    
    plot = plt.plot(df['time'],df['LRF'])
    plt.plot(df['time'],df['SMA10'])
    plt.xlabel("Time (years)")
    plt.title(key)
    plt.show()
    plt.savefig(plot_path + key + ".jpg")
    plt.clf()
    return plot