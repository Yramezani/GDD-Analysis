'''Reads data files in input folder(home by default, -Gi is flag for passing new one) then calls GDDcalculator.py,
 passes lists of maximum and minimum temperatures also base and upper, takes list of GDD from that and concatenates it
 with associated Data Frame'''
from GDDcalculate import *
import argparse
import pandas as pd
import glob

print("GDD.py starts")
parser = argparse.ArgumentParser(description="Calculating GDD")  # Argument parser for command-line friendly script
parser.add_argument("-tbase", "-b", type=float, help="Base temperature")  # takes base temperature
parser.add_argument("-tupper", "-u", type=float, help="Upper temperature")  # takes upper temperature
parser.add_argument("-GDDinfolder", "-Gi", type=str, default="./", help="Folder containing GDD input files.")
parser.add_argument("-GDDoutfolder", "-Go", type=str, default="./", help="Folder that will keep GDD output files.")

args = parser.parse_args()

for fname in glob.glob(args.GDDinfolder + "*.csv"):  # For loop for .csv files in given input folder
    D = pd.read_csv(fname, skiprows=22, header=1)  # skipped rows will change if data frame's shape change###############IMPORTANT
    df = pd.DataFrame(D)
    print(df.columns.values)

    tempmax = df['Max Temp (°C)']
    tempmin = df['Min Temp (°C)']  # Data frame's column

    year = list(df['Year'])[1]  # Just so that we can name final file!

    length = len(pd.Series.dropna(tempmin))  # omits None values and gets actual length

    GDD = GDDcalculate(list(tempmin), list(tempmax), args.tbase, args.tupper, length)  # Calls GDD calculator
    df["GDD"] = GDD  # Adds new columnsto Data frame
    df.to_csv(args.GDDoutfolder + str(args.tbase) + "_" + str(args.tupper)+"_"+str(year)+ "_GDD.csv")
