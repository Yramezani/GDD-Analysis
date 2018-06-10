import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np
import glob
import os
import sys
import datetime
path = "/home/jovyan/lectures/Data/*.csv"
myfiles=[]
for fname in glob.glob(path):#finds the GDD file in the specified path
    Data=pd.read_csv(fname,usecols=['Date/Time','GDD'],parse_dates=['Date/Time'])
    df=pd.DataFrame(Data)
    cleandata=clean_data(df)#cleans the obtained raw data
    df.to_csv('GDD.csv')
Cumulative_GDD = np.cumsum( df['GDD'])
x=df['Date/Time']
plt.plot(x,Cumulative_GDD,color="green")
plt.legend(loc='upper right')
plt.xlabel('Year')
plt.ylabel('cumulative growing degree days(>50°F)')
plt.title("(st.johns)2017-Growing Degree days comparision(>50°F)")
plt.grid(True)
plt.annotate("Cumulative Growing degree days\n"
                 "as of January 2017\n"
                ,(0.3, 0.8),
                 xycoords="axes fraction", va="center", ha="center",
                 bbox=dict(boxstyle="square, pad=1", fc="w"))
plt.show()

