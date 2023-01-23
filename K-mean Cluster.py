#!/usr/bin/env python
# coding: utf-8

# In[6]:


from sklearn.cluster import KMeans
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from matplotlib import pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[7]:


df=pd.read_csv("MSN Content Syndication November 22.csv")
df.head()


# In[13]:


plt.scatter(df["Brand (Provider)"],df["Content Partner RevShare"])


# In[ ]:




