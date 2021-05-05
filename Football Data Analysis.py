#!/usr/bin/env python
# coding: utf-8

# # Fifa Players Analysis

# In[21]:


import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns


# In[22]:


fifa = pd.read_csv(r"C:\Users\user\Downloads\fifa data.csv")


# In[23]:


fifa.head()


# In[25]:


for col in fifa.columns:
    print(col)


# In[27]:


fifa.shape


# In[30]:


fifa['nationality'].value_countss()


# In[31]:


fifa['nationality'].value_counts()[0:10]


# In[33]:


fifa['nationality'].value_counts()[0:5].keys()


# In[51]:


plt.figure(figsize=(8,5))
plt.bar(list(fifa['nationality'].value_counts()[0:10].keys()),list(fifa['nationality'].value_counts()[0:10]),color=["r","b","g","black","purple","y","gray","pink","orange","b"])
plt.show()


# In[48]:


p_salary= fifa[['short_name','wage_eur']]
p_salary.head()


# In[49]:


p_salary=p_salary.sort_values(by=['wage_eur'],ascending=False)
p_salary.head()


# In[60]:


plt.figure(figsize=(8,5))
plt.bar(list(p_salary['short_name'][0:5]),list(p_salary['wage_eur'][0:5]), color=["r","b","g","black","purple","y","gray","pink","orange","gray"])
plt.show()


# In[61]:


fifa['nationality']=='England'


# # England

# In[63]:


England=fifa[fifa['nationality']=='England']
England.head(10)


# In[64]:


England.sort_values(by=['height_cm'],ascending=False).head()


# In[71]:


England.sort_values(by=['weight_kg'],ascending=False).head()


# In[72]:


England.sort_values(by=['wage_eur'],ascending=False).head()


# In[75]:


England[['short_name','wage_eur']].sort_values(by=['wage_eur'],ascending=False).head()


# # Shooting

# In[103]:


Shooting= fifa[['short_name','shooting','nationality','club']]


# In[104]:


Shooting.sort_values(by=['shooting'],ascending=False).head()


# # Defending

# In[111]:


Defending= fifa[['short_name','defending','nationality','club']]


# In[112]:


Defending.sort_values(by=['defending'],ascending=False).head()


# # Club

# In[94]:


FCB=fifa[fifa['club']=='FC Barcelona']


# In[95]:


FCB.sort_values(by=['wage_eur'],ascending=False).head()


# In[99]:


FCB.sort_values(by=['shooting'],ascending=False).head()


# In[100]:


FCB.sort_values(by=['defending'],ascending=False).head()


# In[106]:


FCB['nationality'].value_counts()


# In[ ]:




