import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import glob

Sum = [np.nan] * 365
average = []
for fname in glob.glob("*GDD.csv"):  # For loop for .csv files in current folder
    D = pd.read_csv(fname, header=0)  # skipped rows will change if data frame's shape change
    df = pd.DataFrame(D)
    print("Accessing headers of " + fname)

    year = list(df['Year'])[1]
    df = df[df["Date/Time"] != str(year) + "-02-29"]  # Deletes Febuary 29th from leap year's data
    t = list(df["GDD"])
    a = np.array([t, Sum])
    average = np.nanmean(a, axis=0)
    Sum += average

x = df["Date/Time"]
year = list(df['Year'])[1]
plt.plot(x, average, color="red", label="Average")
plt.scatter(x, t, label=str(year))

U = np.array(average) * 1.05
D = np.array(average) * 0.95
plt.fill_between(x, U, D, alpha=0.3, color='blue', label="5-95 percentile")

Uu = np.array(average) * 1.25
Dd = np.array(average) * 0.75
plt.fill_between(x, Uu, Dd, alpha=0.3, color='red', label="25-75 percentile")

plt.xlabel('time')
plt.ylabel('Daily Accumulation (Celicius)')
plt.title('Daily Growing degree days')
plt.grid(True)
plt.tight_layout()

plt.xticks([0, 30, 58, 89, 119, 150, 180, 211, 242, 272, 303, 333],
           ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])