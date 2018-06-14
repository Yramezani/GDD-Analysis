
# coding: utf-8

# In[4]:


""" this function takes GDD values from a .csv file and creates a bokeh plot of the cumulative GDD value through the year"""

from bokeh.plotting import figure, output_file, show, save
from bokeh.models import HoverTool, BoxSelectTool
import pandas as pd
import numpy as np
import os
import sys
import glob


# In[10]:


def make_bokehplot(filename): #input CSV file with GDD values
    for filename in glob.glob("./input/Montreal_2017*"): 
        D = pd.read_csv(filename)
        df = pd.DataFrame(D)
        df.index
        accum_GDD = np.cumsum(df['GDD']) #sums the daily GDD values to make them accumulated

   

    
        fig = figure(tools="pan,box_zoom,wheel_zoom,reset,save,hover,box_select", plot_width = 700, plot_height = 700, 
           title = "Accumulated GDD for Montreal in 2017", 
                x_axis_label = 'Year (in days)', y_axis_label = 'Calculated GDD')

        
        hover = HoverTool(
            tooltips=[
                ("Day of year", "$index"), 
                ("GDD value", "$accum_GDD")
                    ]
                )

        fig.circle(df.index, accum_GDD, size=9, color='green', alpha=0.5)
        
        # save to html...
        
#         basename = os.path.basename(filename) # mydir/12345.csv -> 12345
#         output = basename + '_bokeh.html'
        
        ### absolutely could not get the output to save in another folder, arugments needed commented out below
        
        output_file('montreal_2017.html', title="Accum. GDD for Montreal") # mode='relative(-dev)', root_dir= notebooks/CMSC/Project/bokeh_plot
        
        show(fig)


# In[11]:


make_bokehplot("./input/Montreal_2017*")

