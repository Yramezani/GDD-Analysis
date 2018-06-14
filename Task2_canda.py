import cartopy.crs as ccrs
import matplotlib.pyplot as plt
tbase=50
tupper=10
T=[]
#co-ordinates
mylat_Mont=45.48
mylong_Mont=-73.55
mylat_Toronto=44.19
mylong_Toronto=-79.66
fig = plt.figure(figsize=(10,20))
for fname in glob.glob('./input/Montreal*'):
    print(fname)
    Data=pd.read_csv(fname,header=0)
    df=pd.DataFrame(Data)
    year = df['Year'].unique()
    t = list(df["GDD"])
    T.append(t) 
#     average = np.nanmean(np.array(T))
    Cumulative_GDD = np.cumsum(np.array(T))
ax = plt.axes(projection=ccrs.PlateCarree())
ax.set_extent([-145,-50,40,70])
#plotting according to latitude and logitude positions
ax.plot(mylong_Mont, mylat_Mont,
         color='red', linestyle='--',
         transform=ccrs.PlateCarree(),
         marker='o')
ax.plot(mylong_Toronto, mylat_Toronto,
         color='red', linestyle='--',
         transform=ccrs.PlateCarree(),
         marker='o')
ax.coastlines()
ax.text(mylong_Mont+3, mylat_Mont, 'Montreal',
         horizontalalignment='right',
         transform=ccrs.Geodetic())

ax.text(mylong_Toronto-3, mylat_Toronto, 'Toronto',
         horizontalalignment='left',
         transform=ccrs.Geodetic())

plt.show()
plt.savefig('./docs/GDD_Canada.png')
