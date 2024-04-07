#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as pt
import numpy as np
import seaborn as sns


# In[2]:


df = pd.read_csv(r"/Users/g.mahima/Downloads/Chennai_1990_2022_Madras.csv") #printing dataframe


# In[3]:


df


# In[4]:


df.describe()


# DATA CLEANING

# In[5]:


df.isna().sum()


# In[6]:


sns.heatmap(df.isnull())


# In[7]:


df.drop_duplicates()


# In[8]:


df['tmin'].value_counts()


# In[9]:


df['tavg'].value_counts()


# In[10]:


df['tavg']=df['tavg'].fillna(method = 'ffill')


# In[11]:


df.isna().sum()


# In[12]:


df['tmax']=df['tmax'].fillna(method='ffill')


# df.isna().sum()

# In[13]:


df.isna().sum()


# In[14]:


df['prcp']=df['prcp'].fillna(0)
df['tmin']=df['tmin'].fillna(method='ffill')


# In[15]:


df.isna().sum()


# In[16]:


df.isna().sum()    #all null values removed


# In[17]:


df.dtypes     #checking data types


# In[18]:


df['time'] = pd.to_datetime(df['time'],dayfirst= True) #converting datatypes
df['tavg'] = pd.to_numeric(df['tavg'])


# DATA VISUALIZATION

# In[19]:


df=df.set_index('time')   #using date as index from now
df[0:365].plot(kind='line', subplots = True, title = 'Weather Data', xlabel='Date', ylabel = 'values')


# In[20]:


#kind-for type of plot 
#Subplots- to split plotting 
#title- naming graphs
#xlabel and ylabel- to give labels to the x and y axis


# In[21]:


df.plot(kind='scatter',x='tmin',y='prcp')


# In[22]:


df.plot(kind='scatter',x='tmax',y='prcp')


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




