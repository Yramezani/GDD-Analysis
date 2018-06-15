'''A double-bar plot of April's maximum and Minimum temperatures of each day'''
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import glob
Min = [100]*30 #a bviously big number to make sure others will be smaller
Max = [-100]*30
for fname in glob.glob("./input/Montreal*"):  # For loop for .csv files in given input folder
    D = pd.read_csv(fname, header=0)  # skipped rows will change if data frame's shape change
    df = pd.DataFrame(D)
    year = list(df['Year'])[1]
    df = df[df["Date/Time"] != str(year)+"-02-29"]
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
width = 0.40
plt.bar(ind, Min, width, label='Min',color='blue')
plt.bar(ind + width, Max, width, label='Max',color='red')

plt.ylabel('Days')
plt.title('Maximum and Minimum daily tempratures of April from 2014 to 2017, Montreal')

plt.xticks(ind + width / 2, np.arange(N)+1)
plt.legend(loc='best')
plt.xticks(rotation=90)
plt.tight_layout()
# plt.show()
fig = plt.gcf()
fig.set_size_inches(18.5, 10.5)
fig.savefig('test2png.png', dpi=100)
plt.savefig('./docs/aprildaily.png')
