### DownloadData.py modules will download data files for three cities: Victoria, Montreal, Toronto from 2014 to 2017. They will be saved in ./input.
### GDD.py can be called via command line, inputs would be of the form:
### GDD.py base_temperature upper_temperature Input_folder Output_folder
* base_temperature :
  - "-tbase", "-b", type=float, default=10
* upper_temperature :
  - "-tupper", "-u", type=float, default=30, help="Upper temperature")
* Input_folder :
  - "-GDDinfolder", "-Gi", type=str, default="./input/", help="Folder containing GDD input files.")
* Output_folder:
  - "-GDDoutfolder", "-Go", type=str, default="./input/", help="Folder that will keep GDD output files."
### GDD.py calls GDDcalculate.py to calculate GDD for each and every .csv file in ./input and will add a GDD column to data file. Even though input and output folder can be changed for GDD.py, it's not recomended as all other modules are set to look into ./input repository.
### GDD_plot.py will plot the cumulative Growing degree days for : Victoria, Montreal, Toronto from 2014 to 2017. It will creat 3 .png files namely : Victoria.GDD.png, MontrealGDD.png, TorontoGDD.png in ./docs folder.
### MinMaxplot.py will plot Annual cycle of Min and Max daily temperatures of Victoria, Montreal, Toronto from 2014 to 2017. It will creat 3 .png files namely : Min_Max_Temp_Victoria.png ...in ./docs folder.
### GDD_bokeh.py  takes GDD values from a .csv file and creates a bokeh plot of the cumulative GDD value through the year.
### aprildaily.py creats double-bar plot of April's maximum and Minimum temperatures of each day. result is saved as aprildaily.png in ./docs
### histograms.py shows a figure containing two plots. Upper one, is histogram for both minimum and maximum temperatures for first 6 months of year. lower one is histogram of mean temperature for the same range of time'. results are saved as hostogram2014/5/6/7.png
### task1.py module plots average of GDD for couple of years, and also its percentile of 5-95 and 25-75 as a band. It also shows scatter plot of GDD for last year involved in calculations. out put is saved in ./docs as task1.png
### test_gdd.py tests GDDcalculator.py by passing variant inputs

* To run programs python 3 is needed. list of necessary packages are:
- matplotlib.pyplot as plt	
- pathlib	argparse		
- from bokeh.plotting import figure, output_file, show, save	from bokeh.models 
- HoverTool, BoxSelectTool		 
- pandas as pd	
- numpy as np	
- os	
- sys	
- glob
