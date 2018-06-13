
# coding: utf-8

# In[2]:




import os
import urllib.request
import sys
import pandas as pd
import numpy as np
import pathlib


""" Script for downloading data
    this function will download and then save a csv file 
    that has the required columns for our further calculations and plots.
    
Return:
    string: this is a string value that defines the *.csv file that was downloaded/stored.
"""
def download(Namecity,year,inputfolder="csv_data"):
    
    print("Started downloading ...")

    stationid= Ncity_to_stationID(Namecity, year)
    print("Data for station with id {} for year {}".format(stationid, year))
     
    fname = "{}_{}_t.csv".format(stationid, year)
    url = "http://climate.weather.gc.ca/climate_data/bulk_data_e.html?format=csv&stationID="+str(stationid)+"&Year="+str(year)+"&Month=8&Day=1&timeframe=2&submit=Download+Data"

    try:
        urllib.request.urlretrieve(url, fname)
    except FileNotFoundError as fnfe:
        print("File not found error")
        print("%s" % fnfe)
        return ""
    except Exception as e:
        print("%s" % e)
        return ""

    print("Download completed...")
    print("Extracting required columns...")

    data_frame = pd.read_csv(fname, skiprows=22, header=1, sep=",", encoding="ISO-8859-1")
    columns =range (0,10)
    df = data_frame.iloc[:,columns]
    
    #df=clean_data(df)
    #print(df)
    #df_rename = df.columns=["Date/Time","Year","Month","Day","Data Quality","Max Temp (°C)","Max Temp Flag","Min Temp (°C)","Min Temp Flag","Mean Temp (°C)"]
    pathlib.Path('../' + str('inputfolder')).mkdir(parents=True, exist_ok=True)
    df.to_csv("../" + str('inputfolder') + "/{}_{}.csv".format(Namecity, year))
    #new_fname =  os.path.dirname(os.path.realpath(__file__)) + "/../inputfolder/{}_{}.csv".format(Namecity, year)
    #df.to_csv(new_fname)
    #print("File saved into: " + new_fname)
     #data.to_csv("./Input/"+str(year)+"_"+city+"_temp.csv")
    # removing temporary saved file
    os.remove(fname)
    #print(df)
    print("File saved.")



# In[41]:



# coding: utf-8

# In[ ]:


def Ncity_to_stationID(Namecity, year):

    stations1 = {'St. John\'s': 50089, 

                'Yellowknife': 51058,

                'Charlottetown': 50621, 

                'Halifax': 50620,

                'Fredericton': 48568, 

                'Ottawa': 49568,

                'Winnepeg': 51097,

                'Regina': 28011,

                'Edmonton': 50149,

                'Victoria': 51337,
                  'Toronto':51459,

                'Quebec City': 26892,

                'Whitehorse': 50842,

                'Montreal':51157,

                'Iqaluit': 42503}

    stations2 = {'St. John\'s': 6720,
                'Toronto':5097,

                'Yellowknife': 1706,

                'Charlottetown': 6526, 

                'Halifax': 6358,

                'Fredericton': 6157, 

                'Ottawa': 49568,

                'Winnepeg': 51097,

                'Regina': 3002,

                'Edmonton': 1865,

                'Victoria': 118,

                'Quebec City': 26892,

                'Whitehorse': 1617,

                'Montreal':51157,

                'Iqaluit': 1758}

    if year >= 2012 :
        return stations1[Namecity]
    else:
        return stations2[Namecity]



# In[42]:


def clean_data(dataframe):
    """
    Then Remove all the 'NAN' data in csv data file
    """
    dataframe.replace('E', np.nan,inplace=True)

    dataframe.replace('M', np.nan,inplace=True)

    data = dataframe.dropna()

    dataframe=data

    return dataframe



# In[43]:
#download()
#download(inputfolder="csv_data")


