'''Shows a figure containing two plots. Upper one, is histogram for both minimum and maximum temperatures for first 6
months of year. lower one is histogram of mean temperature for the same range of time'''
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import glob

f = 1
for fname in glob.glob("./input/Montreal*"):  # For loop for .csv files in given input folder
    D = pd.read_csv(fname, header=0)  # skipped rows will change if data frame's shape change
    df = pd.DataFrame(D)
    year = list(df['Year'])[1]
    df = df[df["Date/Time"] != str(year)+"-02-29"]
    df = df[df["Month"] < 6]  # Takes data for April and discards the rest
    dfmax = df["Max Temp (°C)"]
    dfmin = df["Min Temp (°C)"]
    dfmean = df["Mean Temp (°C)"]
    x = df["Date/Time"]
    plt.figure(f)
    f += 1
    plt.subplot(211)
    plt.hist(dfmax.dropna(), bins=60, color='red', label="Maximum", alpha=0.25)
    plt.title('Maximum and minimum daily temperature histogram for 6 first months of'+str(year)+',Montreal')
    plt.legend(loc='best')
    plt.tight_layout()

    plt.hist(dfmin.dropna(), bins=60, color='blue', label="Minimun", alpha=0.25)
    plt.legend(loc='best')


    plt.subplot(212)
    plt.hist(dfmean.dropna(), bins=60, color='green', label="Mean", alpha=0.7)
    plt.title('Mean daily temperature histogram for 6 first months of '+str(year)+',Montreal')
    plt.legend(loc='best')
    
    fig = plt.gcf()
    fig.set_size_inches(18.5, 10.5)
    fig.savefig('test2png.png', dpi=100)
    plt.savefig('./docs/histogram'+str(year)+'.png')
