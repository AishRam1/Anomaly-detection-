#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import matplotlib.pyplot as pt
import numpy


# In[2]:


df = pd.read_csv(r"/Users/g.mahima/Downloads/weatherdata.csv") #printing dataframe


# In[3]:


df


# In[4]:


df.drop_duplicates()


# In[5]:


df.drop(columns='NAME')
df=df.drop(columns='NAME')


# In[6]:


df


# In[7]:


df["PRCP"].value_counts()


# In[8]:


df['PRCP'] = df["PRCP"].fillna(0)


# In[9]:


df


# In[10]:


df['TMAX'].value_counts()


# In[11]:


df['TMAX'].isna().sum()


# In[12]:


df['TMAX']=df['TMAX'].fillna(method ='pad')


# In[14]:


df
df['TMIN'].isna().sum()


# In[15]:


df['TMIN']=df["TMIN"].fillna(method='pad')


# In[16]:


df


# In[17]:


df.drop(columns="STATION")


# In[18]:


df = df.drop(columns="STATION")


# In[19]:


df


# In[ ]:




