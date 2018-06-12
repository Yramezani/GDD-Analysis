
# coding: utf-8

# In[15]:


from bokeh.plotting import figure, output_file, show
from bokeh.models import HoverTool, BoxSelectTool
import pandas as pd
import numpy as np
import os
import sys


# In[16]:


def make_bokehplot(filename):
    df = pd.read_csv(filename)
    accum_GDD = np.cumsum(df['GDD'])


    basename = os.path.basename(filename) # mydir/12345.csv -> 12345
    output = basename + '_bokeh.html'
    output_file(output, 
                title="Accumulative GDD data for St. John's in 2017")



    fig = figure(tools="pan,box_zoom,wheel_zoom,reset,save,hover,box_select", plot_width = 700, plot_height = 700, 
           title = "Accumulative GDD for St. John's in 2017", x_axis_label = 'Year (in days)', 
             y_axis_label = 'Calculated GDD')

    hover = HoverTool(
        tooltips=[
            ("Day of year", "$index"), 
            ("GDD value", "$accum_GDD")
                ]
            )

    fig.circle(df.index, accum_GDD, size=10, color='purple', alpha=0.5)
    show(fig)
    # save to html...
    


# In[17]:


if __name__=="__main__":
    filename = sys.argv[1]
    city_name = sys.argv[2]
    make_bokehplot(filename)

