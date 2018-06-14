
# coding: utf-8

# In[ ]:


import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np
import glob
import os
import sys
import datetime
import urllib.request
import sys
from sklearn import datasets, linear_model
import csv
from scipy import stats
import pylab
Calculated_GDD=[] 
df = pd.DataFrame()
df2 = pd.DataFrame()
tbase = 10
tupper = 50
startYear=2014
endYear=2016
#The function takes city name and years as input and calcultes Linear Regression for spesific citiy.
def LinearRegressionplots(cityname,tbase, tupper,startYear,endYear):
    """The function takes city name and years as input and calcultes Linear Regression for spesific citiy."""
    years=[2014,2015,2016]
    for year in years:
        for fname in glob.glob('./input/'+str(cityname) + '_' + str(year) + '.csv'):#searches for the specific file in the input folder
            print(str(cityname) + '_' + str(year))
            Data=pd.read_csv(fname,header=0)
            df=pd.DataFrame(Data)
            year = list(df['Year'])[1]
            df = df[df["Date/Time"] != str(year)+"-02-29"]
            tempmax = df['Max Temp (Â°C)']
            tempmin = df['Min Temp (Â°C)'] 
            length = len(pd.Series.dropna(tempmin))
            #calculates the growing degree days based on the following input
            t= GDDcalculate(list(tempmin),list(tempmax), tbase, tupper, length)
            Calculated_GDD.append(t) 
            #calculates the cumulative growing degree days
            Cumulative_GDD=np.cumsum(np.array(Calculated_GDD)) 
        mask = ~np.isnan(Cumulative_GDD)
        Cumulative_GDD=Cumulative_GDD[mask]
        total_gdd = Cumulative_GDD[-1]                        
        df = df.append({'year': int(year), 'gdd': total_gdd}, ignore_index=True)
    x = df.year.values; y = df.gdd.values
    x = x.reshape(x.size,1); y = y.reshape(y.size,1)  

    regr = linear_model.LinearRegression()
    regr.fit(x, y)

    text = "slope: {:0.4}\nscore: {:0.4}".format(regr.coef_[0,0],regr.score(x,y))
    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)
    ax.text(0.05, 0.95, text,backgroundcolor='grey',verticalalignment='top', horizontalalignment='left',transform=ax.transAxes,color='black', fontsize=15)
    ax.scatter(x, y,  color='red')
    ax.plot(x, regr.predict(x), color='blue', linewidth=3)
    ax.set_title('Annual Growing Degree Days in {} from {} to {}'.format(cityname,startYear,endYear))
    ax.set_xlabel('Year')
    ax.set_ylabel('Total GDD')
    plt.savefig('./output/LinearReg_{}_{}_{}.png'.format(cityname,startYear,endYear))
    #plt.savefig('output/Toronto.png')
LinearRegressionplots('Ottawa',10, 50,2014,2016)

