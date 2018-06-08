import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np
Data=pd.read_csv("GDD.csv",usecols=['Date/Time','GDD'],parse_dates=['Date/Time'])
df=pd.DataFrame(Data)
cleandata=clean_data(df)
df.to_csv('GDD.csv')
df.set_index('Date/Time',inplace=True)
fig,ax = plt.subplots(figsize=(7,5))
Cumulative_GDD = np.cumsum( df['GDD'])
ax.plot(Cumulative_GDD,color="green")
ax.legend(loc='upper right')
plt.xlabel('Year')
plt.ylabel('cumulative growing degree days(>50°F)')
plt.title("2017-Growing Degree days comparision(>50°F)")
ax.yaxis.grid(True)
ax.annotate("Cumulative Growing degree days\n"
                 "as of January 2017\n"
                ,(0.25, 0.8),
                 xycoords="axes fraction", va="center", ha="center",
                 bbox=dict(boxstyle="square, pad=1", fc="w"))
plt.show()
