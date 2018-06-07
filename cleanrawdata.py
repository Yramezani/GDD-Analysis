
# coding: utf-8

# In[ ]:


def clean_data(dataframe):
"""
Then Remove all the 'NAN' data in csv data file
"""
    dataframe.replace('E', np.nan,inplace=True)

    dataframe.replace('M', np.nan,inplace=True)

    data = dataframe.dropna(how='any')

    dataframe=data

    return dataframe

