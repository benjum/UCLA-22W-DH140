#!/usr/bin/env python
# coding: utf-8

# # Pandas & Seaborn

# <img src='assets/helpers/pandas.png' width=400>
# 
# Pandas is Python software library for manipulating and analyzing data.  
# 
# It may be one of the most widely used tools for data munging
# * present data in nice formats
# * multiple convenient methods for filtering data
# * work with a variety of data formats (CSV, Excel, …)
# * convenient functions for quickly plotting data

# ## Importing libraries and Setting up some data

# In[ ]:


import yahoo_fin.stock_info as si
import requests
import pandas as pd
import matplotlib.pyplot as plt
import ipywidgets


# In[ ]:


# Getting the actual company name from a stock ticker symbol
def get_symbol(symbol):
    url = "http://d.yimg.com/autoc.finance.yahoo.com/autoc?query={}&region=1&lang=en".format(symbol)
    result = requests.get(url).json()
    for x in result['ResultSet']['Result']:
        if x['symbol'] == symbol:
            return x['name']


# In[ ]:


get_symbol('AAPL')


# In[ ]:


few_days = si.get_data('aapl', start_date = '01/01/2020', end_date = '03/31/2021')


# In[ ]:


few_days


# In[ ]:


# The Matplotlib way

fig,ax = plt.subplots(1,1,figsize=(7,5))
ax.plot(few_days.index, few_days.high)
ax.set_title(get_symbol('AAPL'))
fig.autofmt_xdate()


# In[ ]:


# The Pandas way

few_days.plot(y='high');


# In[ ]:


few_days.plot(y='high',
              figsize=(7,5),
              title=get_symbol('AAPL'),
              legend=False);


# ## There are also methods for conveniently making a range of other plots

# In[ ]:


appl_top_6 = pd.read_csv('assets/helpers/holdings-of-appl-top-6.csv')


# In[ ]:


appl_top_6


# In[ ]:


appl_top_6.plot.bar(x='Company');


# In[ ]:


appl_top_6.sort_values('Vanguard Group, Inc. (The)')


# In[ ]:


appl_top_6.sort_values('Vanguard Group, Inc. (The)').plot.bar(x='Company',
                                                              figsize=(15,7),
                                                              cmap='gist_rainbow');


# In[ ]:


vang_top_5 = appl_top_6.sort_values('Vanguard Group, Inc. (The)',ascending=False)[:5]
vang_top_5


# In[ ]:


vang_top_5.plot.barh(x='Company',
                     figsize=(10,7),
                     cmap='gist_rainbow');


# In[ ]:


vang_top_5.plot.barh(x='Company',
                     figsize=(10,7),
                     cmap='gist_rainbow');

# You can use plt.gca to get the current axes object from pandas plots too
# and then use regular matplotlib methods to alter the plots
# Try doing that here to change limits on the horizontal axis to (0,15)
# and then make xticks of (0,5,10,15)



# In[ ]:


get_ipython().run_line_magic('load', '"assets/helpers/vanguard5.py"')


# # Seaborn
# 
# If Matplotlib 'tries to make easy things easy and hard things possible,' Seaborn tries to make a well-defined set of hard things easy too.
# 
# https://seaborn.pydata.org
# 
# <img src='assets/helpers/seaborn.png' width=700>
#           
# * Built on top of matplotlib and closely integrated with pandas data structures.
# * Used for making statistical graphics and using visualization to quickly and easily explore and understand data.
# * The style settings can also affect matplotlib plots, even if you don't make them with seaborn.

# In[ ]:


import seaborn as sns


# In[ ]:


sns.scatterplot(data=appl_top_6, x="Blackrock Inc.", y="Vanguard Group, Inc. (The)");


# In[ ]:


sns.lmplot(data=appl_top_6, x="Blackrock Inc.", y="Vanguard Group, Inc. (The)");


# In[ ]:


sns.pairplot(appl_top_6.loc[:,appl_top_6.columns != 'Company']);


# In[ ]:


df = sns.load_dataset("iris")
df.head()


# In[ ]:


sns.set(style="whitegrid")
# sns.set(style="dark")


# In[ ]:


sns.scatterplot(x=df.petal_length,y=df.petal_width,style=df.species);


# In[ ]:


sns.scatterplot(x=df.petal_length,y=df.petal_width,hue=df.species);


# In[ ]:


sns.pairplot(df,hue='species');


# In[ ]:


sns.regplot(x=df.petal_length,y=df.petal_width);


# In[ ]:


g = sns.FacetGrid(df, col='species', hue='species')
g.map(plt.scatter, 'petal_length', 'petal_width');


# # Preview of next week

# In[ ]:


import plotly.express as px


# In[ ]:


fig = px.scatter(df, x='petal_length', y='petal_width', color="species")
fig.show()


# In[ ]:


px.scatter_3d(df,x='petal_length',y='petal_width',z='sepal_length',color='species')


# In[ ]:


def plotdows(ticker='AAPL'):
    few_days = si.get_data(ticker, start_date = '01/01/2020', end_date = '03/31/2021')
    fig,ax = plt.subplots(1,1,figsize=(7,5))
    ax.plot(few_days.index, few_days.high)
    ax.set_title(get_symbol(ticker))
    fig.autofmt_xdate()
    
dow_list = si.tickers_dow()
ipywidgets.interactive(plotdows,ticker=dow_list)

