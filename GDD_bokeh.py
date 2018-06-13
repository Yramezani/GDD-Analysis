
# coding: utf-8

# In[63]:


from bokeh.plotting import figure, output_file, show, save
from bokeh.models import HoverTool, BoxSelectTool
import pandas as pd
import numpy as np
import os
import sys
import glob


# In[96]:


""" this function takes GDD values from a .csv file and creates a bokeh plot of the cumulative GDD value through the year"""

def make_bokehplot(filename): #input CSV file with GDD values
    for filename in glob.glob("*GDD.csv"): 
        D = pd.read_csv(filename)
        df = pd.DataFrame(D)
        df.index
        accum_GDD = np.cumsum(df['GDD']) #sums the daily GDD values to make them accumulated

        #### Uncomment 3 lines below for accurate title from dataframes #####
    
#         fig = figure(tools="pan,box_zoom,wheel_zoom,reset,save,hover,box_select", plot_width = 700, plot_height = 700, 
#            title = "Accumulative GDD for "  + str(list(df["Name"])[1]) +  " in "  + str(list(df["Year"])[1]), 
#                 x_axis_label = 'Year (in days)', y_axis_label = 'Calculated GDD')
        
        #### Comment 3 lines below if uncommenting above #####
    
        fig = figure(tools="pan,box_zoom,wheel_zoom,reset,save,hover,box_select", plot_width = 700, plot_height = 700, 
           title = "Accumulated GDD for CITY in YEAR", 
                x_axis_label = 'Year (in days)', y_axis_label = 'Calculated GDD')

        ####
        
        hover = HoverTool(
            tooltips=[
                ("Day of year", "$index"), 
                ("GDD value", "$accum_GDD")
                    ]
                )

        fig.circle(df.index, accum_GDD, size=9, color='green', alpha=0.5)
        
        # save to html...
        
        basename = os.path.basename(filename) # mydir/12345.csv -> 12345
        output = basename + '_bokeh.html'
        
        ### absolutely could not get the output to save in another folder, arugments needed commented out below
        
        output_file(output, title="Accum. GDD") # mode='relative(-dev)', root_dir= notebooks/CMSC/Project/bokeh_plot
        
        show(fig)

