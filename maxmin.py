import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

D = pd.read_csv("eng-daily-01012018-12312018.csv", skiprows=23, header=1)
df = pd.DataFrame(D)
print(list(df.columns.values))

maxi = df['Max Temp (°C)']
mini = df['Min Temp (°C)']
minimaxi = mini.divide(maxi)

plt.plot(df["Date/Time"].tolist(),minimaxi.tolist())
plt.title('Annual min/max')
plt.ylabel('min/max')
plt.xlabel('Days')
plt.xticks(np.arange(0, 365, 30),('1', '30', '60', '90', '120','150','180','210','240','270','300','330','360'))
plt.grid(True)

