import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import glob
import pathlib

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


def clean_data(dataframe):
    """
    Then Remove all the 'NAN' data in csv data file
    """
    dataframe.replace('E', np.nan,inplace=True)
    dataframe.replace('M', np.nan,inplace=True)
    data = dataframe.dropna(how='any')
    dataframe=data

    return dataframe
import os
import urllib.request
import sys
import pandas as pd


""" Script for downloading data
    this function will download and then save a csv file 
    that has the required columns for our further calculations and plots.
    
Return:
    string: this is a string value that defines the *.csv file that was downloaded/stored.
"""
def download(Namecity, year, inputfolder="input"):
    print("Started downloading ...")
    stationid= Ncity_to_stationID(Namecity, year) 
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
    data_frame = data_frame.iloc[:,columns]
#     data_frame=clean_data(data_frame)
    data_frame["Name"] = [str(Namecity)]*len(data_frame["Date/Time"])
    pathlib.Path('./'+str(inputfolder)).mkdir(parents=True, exist_ok=True)
    data_frame.to_csv("./"+str(inputfolder)+"/{}_{}.csv".format(Namecity, year))
    print("File saved into: "+str(inputfolder))
    os.remove(fname)
    print("File saved.")

cityname=['Victoria','Montreal','Ottawa']
years=[2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017]
for i in cityname:
    for j in years:
        download(i, j, inputfolder="input")
