
# coding: utf-8

# In[66]:


from bokeh.plotting import figure, output_file, show
from bokeh.models import HoverTool, BoxSelectTool
import pandas as pd
import numpy as np


# In[67]:


df.index


# In[81]:


df = pd.read_csv('0.0_30.0_2017_GDD.csv')
accum_GDD = np.cumsum(df['GDD'])


output_file("gdd_bokeh.html", title="Accumulative GDD data for St. John's in 2017")



fig = figure(tools="pan,box_zoom,wheel_zoom,reset,save,hover,box_select", plot_width = 700, plot_height = 700, 
           title = "Accumulative GDD for St. John's in 2017", x_axis_label = 'Year (in days)', 
             y_axis_label = 'Calculated GDD')

# hover = HoverTool(
#     tooltips=[
#         ("Day of year", "$index"), 
#         ("GDD value", "$accum_GDD")
#         ]
#     )

fig.circle(df.index, accum_GDD, size=10, color='purple', alpha=0.5)
show(fig)

