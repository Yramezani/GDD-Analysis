
# coding: utf-8

# In[ ]:


def LinearRegresion(fname1,fname2,fname3):
    import pandas as pd
    import csv
    import sys
    from scipy import stats
    import numpy as np
    import pylab
    df2=fname1
    df1=fname2
    df=fname3
    data_to_plot2=[df,df1,df2]
    #To remove None from the argv
    data_to_plot = [x for x in data_to_plot2 if x is not None]
    #To iterate each file_name in the function analyze_gdd
    for i in data_to_plot:
    #get data, year, month,day and mean_temp from read_weather_analyze() function
        data,year,month,day,mean_temp=read_weather_analyze(i)
        #To replace data has 0 to NAN, because we do not need 0 data to plot gdd
        data.replace('0',np.nan,inplace=True)
        #To remove all the NAN data
        data=data.dropna(how='any')
        #To convert date type into integer data type for linear regression
        x=100*month + day
    #x= day
    #print(x)
        #To put the x into frames_x list
        frames_x= [x]
    #print(frames_x)
        #In this case, the t-base is 10,then gdd would be mean_temp-10, and save the gdd into frames_y list
        frames_y= [mean_temp-10]
    #print(frames_y)
    #To takes frames_x list and concatenates them to x 
    x = pd.concat(frames_x)
#print(x)
    #To takes frames_y list and concatenates them to y 
    y=  pd.concat(frames_y)
    #print(y)
    #To remove NaNs in the data using a mask:
    mask = ~np.isnan(x) & ~np.isnan(y)
    #Calculate a linear least-squares regression for two sets of measurements and remove all NAN in x and y
    #and to get estimates of the slope and intercept parameters.
    slope, intercept, r_value, p_value, slope_std_error = stats.linregress(x[mask], y[mask])
#print(slope_std_error)
#print(intercept)
    #To get predict_y by the following function
    predict_y = intercept + slope * x  
    fig,ax1=plt.subplots()
    #To set x-axis label
    ax1.set_xlabel('Time')
    #To set y-axis label
    ax1.set_ylabel('Expected Result')
    #To set the title in the linear regression plot graph
    ax1.set_title('linear regression')
    #first to plot x and y
    pylab.plot(x, y, 'o',label='original data')
    #second to plot liner regression
    pylab.plot(x, predict_y, 'k-',label='fitted line')
    plt.legend()
    plt.show()
    #analyze_gdd=plt.savefig("analyze_gdd.png",format="png")

