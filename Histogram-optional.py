import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import glob

f = 1
for fname in glob.glob("*GDD.csv"):  # For loop for .csv files in given input folder
    D = pd.read_csv(fname, header=0)  # skipped rows will change if data frame's shape change
    df = pd.DataFrame(D)
    df = df[df["Month"] < 6]  # Takes data for April and discards the rest
    dfmax = df["Max Temp (°C)"]
    dfmin = df["Min Temp (°C)"]
    dfmean = df["Mean Temp (°C)"]
    x = df["Date/Time"]
    plt.figure(f)
    f += 1
    plt.subplot(211)
    plt.hist(dfmax.dropna(), bins=60, color='red', label="Maximum", alpha=0.25)
    plt.legend(loc='best')
    plt.tight_layout()

    plt.hist(dfmin.dropna(), bins=60, color='blue', label="Minimun", alpha=0.25)
    plt.legend(loc='best')
    plt.tight_layout()

    plt.subplot(212)
    plt.hist(dfmean.dropna(), bins=60, color='green', label="Mean", alpha=0.7)
    plt.legend(loc='best')
    plt.tight_layout()