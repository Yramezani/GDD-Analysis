'''A double-bar plot of April's maximum and Minimum temperatures of each day'''
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import glob
Min = [0]*30
Max = [0]*30
for fname in glob.glob("*GDD.csv"):  # For loop for .csv files in given input folder
    D = pd.read_csv(fname, header=0)  # skipped rows will change if data frame's shape change
    df = pd.DataFrame(D)
    df = df[df["Month"] == 4]  # Takes data for April and discards the rest
    dfmax = list(df["Max Temp (°C)"])
    dfmin = list(df["Min Temp (°C)"])
    for i, t in enumerate(dfmax):   # compares each day's temperature to the value already in list. holds the maximum.
        if Max[i] < t:
            Max[i] = t
    for i, t in enumerate(dfmin):
        if Min[i] > t:
            Min[i] = t
N = 30
ind = np.arange(N)
width = 0.35
plt.bar(ind, Min, width, label='Min')
plt.bar(ind + width, Max, width, label='Max')

plt.ylabel('Days')
plt.title('Maximum and minimum temperatures in April')

plt.xticks(ind + width / 2, np.arange(N)+1)
plt.legend(loc='best')
plt.tight_layout()
plt.show()
