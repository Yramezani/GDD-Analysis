import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np
import glob
import os
import sys
import datetime

################################This script will plot the cumulative Growing degree days for selected cities#######################

Calculated_GDD=[] 
tbase = 10
tupper = 50
#The function takes city name as input and calcultes Growing degree days and plots with time.
def plots(cityname):
    years=[2014,2015,2017]
    for year in years:
        for fname in glob.glob('./input/'+str(cityname) + '_' + str(year) + '.csv'):#searches for the specific file in the input folder
            print(str(cityname) + '_' + str(year))
            Data=pd.read_csv(fname,header=0)
            df=pd.DataFrame(Data)
            year = df['Year'].unique()
            tempmax = df['Max Temp (Â°C)']
            tempmin = df['Min Temp (Â°C)'] 
            length = len(pd.Series.dropna(tempmin))
            #calculates the growing degree days based on the following input
            t= GDDcalculate(list(tempmin),list(tempmax), tbase, tupper, length)
            Calculated_GDD.append(t) 
            #calculates the cumulative growing degree days
            Cumulative_GDD=np.cumsum(np.array(Calculated_GDD)) 
            Time=np.linspace(1,11,len(Cumulative_GDD))
            #plots the Graph with GDD against Time
            plt.plot(Time,Cumulative_GDD,label=year)
        ax=plt.axes()
        plt.xlabel('Year')
        plt.ylabel('cumulative growing degree days(>50°F)')
        plt.legend(loc='upper right')
        title='Accumulated Growing Degree Days For - ' + str(cityname)
        plt.title(title,color="black", fontsize=16)
        plt.xticks(np.arange(12),('1-Jan', '1-Feb', '1-Mar', '1-Apr', '1-May', '1-Jun', '1-Jul', '1-Aug', '1-Sep', '1-Oct', '1-Nov', '1-Dec'))
        ax.yaxis.grid(True)
        
plots('Victoria')
plt.savefig('output/Victoria.png')#saves the figure into output folder
plt.show()
plots('Montreal')
plt.savefig('output/Montreal.png')
plt.show()
plots('Toronto')
plt.savefig('output/Toronto.png')
plt.show()
