
# coding: utf-8

# In[25]:


from bokeh.plotting import figure, output_file, show
from bokeh.models import HoverTool, BoxSelectTool
import pandas as pd
import numpy as np
import os
import sys
import glob


# In[32]:


def make_bokehplot(filename):
    for filename in glob.glob("*GDD.csv"):
        D = pd.read_csv(filename)
        df = pd.DataFrame(D)
        df.index
        accum_GDD = np.cumsum(df['GDD'])

        fig = figure(tools="pan,box_zoom,wheel_zoom,reset,save,hover,box_select", plot_width = 700, plot_height = 700, 
           title = "Accumulative GDD for St. John's in 2017", x_axis_label = 'Year (in days)', 
             y_axis_label = 'Calculated GDD')

        hover = HoverTool(
            tooltips=[
                ("Day of year", "$index"), 
                ("GDD value", "$accum_GDD")
                    ]
                )

        fig.circle(df.index, accum_GDD, size=9, color='purple', alpha=0.5)
        show(fig)
        # save to html...
        
        basename = os.path.basename(filename) # mydir/12345.csv -> 12345
        output = basename + '_bokeh.html'
        output_file(output, title="Accumulative GDD data for St. John's in 2017")
    


# In[33]:


if __name__=="__main__":
    filename = sys.argv[1]
    city_name = sys.argv[2]
    make_bokehplot(filename)

