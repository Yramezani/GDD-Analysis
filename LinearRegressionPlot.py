import os
import urllib.request
import sys

import pandas as pd
year=2012
fname = "{}_{}_t.csv".format(stationid,year)
url = "http://climate.weather.gc.ca/climate_data/bulk_data_e.html?format=csv&stationID="+str(stationid)+"&Year="+str(year)+"&Month=8&Day=1&timeframe=2&submit=Download+Data"
urllib.request.urlretrieve(url, fname)
data_frame = pd.read_csv(fname, skiprows=22, header=1,sep=",", encoding="ISO-8859-1")
columns = [0,1,2,3,4,5,6,7,8,9]
Data1 = data_frame.iloc[:,columns]
year=2013
fname = "{}_{}_t.csv".format(stationid,year)
url = "http://climate.weather.gc.ca/climate_data/bulk_data_e.html?format=csv&stationID="+str(stationid)+"&Year="+str(year)+"&Month=8&Day=1&timeframe=2&submit=Download+Data"
urllib.request.urlretrieve(url, fname)
data_frame = pd.read_csv(fname, skiprows=22, header=1,sep=",", encoding="ISO-8859-1")
columns = [0,1,2,3,4,5,6,7,8,9]
Data2 = data_frame.iloc[:,columns]
year=2014
fname = "{}_{}_t.csv".format(stationid,year)
url = "http://climate.weather.gc.ca/climate_data/bulk_data_e.html?format=csv&stationID="+str(stationid)+"&Year="+str(year)+"&Month=8&Day=1&timeframe=2&submit=Download+Data"
urllib.request.urlretrieve(url, fname)
data_frame = pd.read_csv(fname, skiprows=22, header=1,sep=",", encoding="ISO-8859-1")
columns = [0,1,2,3,4,5,6,7,8,9]
Data3 = data_frame.iloc[:,columns]
year=2015
fname = "{}_{}_t.csv".format(stationid,year)
url = "http://climate.weather.gc.ca/climate_data/bulk_data_e.html?format=csv&stationID="+str(stationid)+"&Year="+str(year)+"&Month=8&Day=1&timeframe=2&submit=Download+Data"
urllib.request.urlretrieve(url, fname)
data_frame = pd.read_csv(fname, skiprows=22, header=1,sep=",", encoding="ISO-8859-1")
columns = [0,1,2,3,4,5,6,7,8,9]
Data5 = data_frame.iloc[:,columns]
year=2016
fname = "{}_{}_t.csv".format(stationid,year)
url = "http://climate.weather.gc.ca/climate_data/bulk_data_e.html?format=csv&stationID="+str(stationid)+"&Year="+str(year)+"&Month=8&Day=1&timeframe=2&submit=Download+Data"
urllib.request.urlretrieve(url, fname)
data_frame = pd.read_csv(fname, skiprows=22, header=1,sep=",", encoding="ISO-8859-1")
columns = [0,1,2,3,4,5,6,7,8,9]
Data6 = data_frame.iloc[:,columns]
year=2017
fname = "{}_{}_t.csv".format(stationid,year)
url = "http://climate.weather.gc.ca/climate_data/bulk_data_e.html?format=csv&stationID="+str(stationid)+"&Year="+str(year)+"&Month=8&Day=1&timeframe=2&submit=Download+Data"
urllib.request.urlretrieve(url, fname)
data_frame = pd.read_csv(fname, skiprows=22, header=1,sep=",", encoding="ISO-8859-1")
columns = [0,1,2,3,4,5,6,7,8,9]
Data7 = data_frame.iloc[:,columns]
import os
import urllib.request
import sys
import pandas as pd
import numpy as np
from sklearn import datasets, linear_model
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pandas as pd
import csv
import sys
from scipy import stats
import numpy as np
import pylab
from scipy import stats
import scipy as sp
year=2015
startYear=2012
endYear=2017
city='Ottawa'
stationid=50089
df2 = pd.DataFrame()
x_frame = pd.DataFrame()
y_frame = pd.DataFrame()
tbase = 10
tupper = 50
Calculated_GDD=[] 
fname = "{}_{}_t.csv".format(stationid,year)
url = "http://climate.weather.gc.ca/climate_data/bulk_data_e.html?format=csv&stationID="+str(stationid)+"&Year="+str(year)+"&Month=8&Day=1&timeframe=2&submit=Download+Data"
urllib.request.urlretrieve(url, fname)
data_frame = pd.read_csv(fname, skiprows=22, header=1,sep=",", encoding="ISO-8859-1")
columns = [0,1,2,3,4,5,6,7,8,9]
Data4 = data_frame.iloc[:,columns]
Data=[Data1,Data2,Data3,Data4,Data5,Data6,Data7]
years=[2014]
for year in years:
        for i in Data[0:7]:
            df=pd.DataFrame(i)
            year = list(df['Year'])[1]
            df = df[df["Date/Time"] != str(year)+"-02-29"]
            tempmax = df['Max Temp (°C)']
            tempmin = df['Min Temp (°C)'] 
            length = len(pd.Series.dropna(tempmin))
            #calculates the growing degree days based on the following input
            t= GDDcalculate(list(tempmin),list(tempmax), tbase, tupper, length)
            Calculated_GDD.append(t) 
            #calculates the cumulative growing degree days
            Cumulative_GDD=np.cumsum(np.array(Calculated_GDD))
            mask = ~np.isnan(Cumulative_GDD)
            Cumulative_GDD=Cumulative_GDD[mask]
            total_gdd = Cumulative_GDD[-1]                        
            df2= df2.append({'year': int(year), 'gdd': total_gdd}, ignore_index=True)
            print(df2)
            
            #x_frame[i]=year
            #x_frame[i]=total_gdd
#print(df)
x = df2.year.values; y = df2.gdd.values
#x_frame = df2.year.values; y_frame = df2.gdd.values
x = x.reshape(x.size,1); y = y.reshape(y.size,1)  
#print(x)
regr = linear_model.LinearRegression()
regr.fit(x, y)

text = "slope: {:0.4}\nscore: {:0.4}".format(regr.coef_[0,0],regr.score(x,y))
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.text(0.05, 0.95, text,backgroundcolor='grey',verticalalignment='top', horizontalalignment='left',transform=ax.transAxes,color='black', fontsize=15)
ax.scatter(x, y,  color='red')
ax.plot(x, regr.predict(x), color='blue',label='fitted line', linewidth=3)
#ax.plot(x, y, '-',color='red',label='original data')
ax.set_title('Annual Growing Degree Days in {} from {} to {}'.format(city,startYear,endYear))
ax.set_xlabel('Year')
#ax.ylim(0.894, 0.930)
#ax.set_ylim([4750.8, 4751])


ax.set_ylabel('Total GDD')
plt.savefig('./docs/LinReg_{}_{}_{}.png'.format(city,startYear,endYear))
#plt.show()
