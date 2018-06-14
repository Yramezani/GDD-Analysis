
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
import csv
import pylab

def MinMaxPlot(cityname,year):
    ''''will plot annual cycle of Min and Max daily temperatures'''
    for fname in glob.glob('./input/'+str(cityname) + '_' + str(year) + '.csv'):#searches for the specific file in the input folder
            print(str(cityname) + '_' + str(year))
            Data=pd.read_csv(fname,header=0)
            df=pd.DataFrame(Data)
            days=range(0,len(df))                         
            plt.figure(figsize=(15,15))
            temp_Max = df.iloc[:,[5]]
           
            ax2=plt.plot(days, temp_Max,label="Maximum Temp")

            temp_Min= df.iloc[:,[7]]

            ax1=plt.plot(days, temp_Min,label="Minimum Temp")

            plt.xticks([0,30,60,90,120,150,180,210,240,270,300,330,360],
               [r'$Jan$',r'$Feb$',r'$March$',r'$April$',r'$May$',r'$June$',r'$July$',r'$August$',
                                                                 r'$September$',r'$October$',r'$November$',r'$December$',r'$January$'])
            plt.xlim([0,366])

            ax = plt.gca()

            ax.set_xlabel('Days', fontsize=15)

            ax.set_ylabel('Temperature', fontsize=15)

            plt.title('Annual cycle of Min and Max daily temperatures of '+ + str(cityname)+ ' in ' + str(year), color="black", fontsize=18)

            plt.legend(loc='upper right')

            plt.tight_layout(True)

            plt.grid(True)              

    
plots('Victoria')
plt.savefig('output/Victoria.png')
#plt.show()
plots('Montreal')
plt.savefig('output/Montreal.png')
#plt.show()
plots('Toronto')
plt.savefig('output/Toronto.png')
#plt.show()

   

