import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

df=pd.read_csv("GDD.csv",usecols=['Date/Time','GDD'],parse_dates=['Date/Time'])
df.set_index('Date/Time',inplace=True)
fig,ax = plt.subplots(figsize=(9,7))
ax.plot(df['GDD'],color="green")
plt.xlabel('Year')
plt.ylabel('cumulative growing degree days(>50°F)')
plt.title("2017-Growing Degree days comparision(>50°F)")
ax.yaxis.grid(True)
plt.axes([.65, .65, .2, .2])
plt.xticks(())
plt.yticks(())
plt.text(.5, .5, 'Cumulative growing degree days', ha='center', va='center',
        size=7,color='black')
plt.show()
