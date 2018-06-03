from GDDcalculate import *
import argparse
import pandas as pd
import glob

parser = argparse.ArgumentParser(description="Calculating GDD")

parser.add_argument("-tbase", "-b", type=float, help="Base temperature")
parser.add_argument("-tupper", "-u", type=float, help="Upper temperature")
parser.add_argument("-GDDinfolder", "-Gi", type=str, default="./", help="Folder containing GDD input files.")
parser.add_argument("-GDDoutfolder", "-Go", type=str, default="./", help="Folder that will keep GDD output files.")

args = parser.parse_args()

for fname in glob.glob(args.GDDinfolder + "*.csv"):  # For loop for .csv files in given input folder
    D = pd.read_csv(fname, skiprows=22, header=1)
    df = pd.DataFrame(D)
    print(df.columns.values)
    tempmax = df['Max Temp (°C)']
    tempmin = df['Min Temp (°C)']
    GDD = GDDcalculate(list(tempmin), list(tempmax), args.tbase, args.tupper)
    print(GDD)
    df["GDD"] = GDD
    output = args.GDDoutfolder + str(args.tbase) + "_" + str(args.tupper) + "_GDD.csv"
    df.to_csv(output)
