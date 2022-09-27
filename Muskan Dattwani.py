#!/usr/bin/env python
# coding: utf-8

# In[101]:


#import libarires which we use:
import warnings
warnings.filterwarnings('ignore')
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[102]:


#read data:
data = pd.read_csv('Salaries.csv')
data


# In[103]:


#finding null values:
data.isnull()


# In[104]:


#sum of all null values:
data.isnull().sum()


# In[105]:


#drop unused columns:
data.drop(columns=['Benefits','Notes', 'Status'], inplace=True)
data


# In[106]:


#final data we can use:
data = data[['BasePay', 'OvertimePay','OtherPay','TotalPay']]
data


# In[107]:


#info of the dataset:
data.info()


# In[108]:


#convert object to numeric:
data.BasePay = pd.to_numeric(data.BasePay, errors='coerce')
data


# In[109]:


#info of the dataset:
data.info()


# In[110]:


#convert object to numeric:
data.OvertimePay = pd.to_numeric(data.OvertimePay, errors='coerce')
data


# In[111]:


#info of the dataset:
data.info()


# In[112]:


#convert object to numeric:
data.OtherPay  = pd.to_numeric(data.OtherPay , errors='coerce')
data


# In[113]:


#info of the dataset:
data.info()


# In[114]:


#drop NaN:
data.dropna(inplace = True)
data


# In[115]:


#describe the dataset:
data.describe()


# In[116]:


#greater than 0:
data = data[data>0]


# In[117]:


#describe the dataset:
data.describe()


# In[118]:


#sum of all null values:
data.isnull().sum()


# In[119]:


#drop NaN:
data.dropna()


# In[120]:


#graph:
plt.hist(data.BasePay)
plt.show()


# In[121]:


plt.hist(data.OvertimePay)
plt.show()


# In[122]:


plt.hist(data.OtherPay)
plt.show()


# In[123]:


plt.hist(data.TotalPay)
plt.show()


# In[124]:


#describe the dataset:
data.describe()


# In[125]:


#quantile function:
mini = data.quantile(0.2)
maxi = data.quantile(0.8)


# In[126]:


data = data[(data>mini) & (data<maxi)]


# In[127]:


#sum of all null values:
data.isnull().sum()


# In[128]:


#drop NaN:
data.dropna(inplace=True)


# In[129]:


#describe the dataset:
data.describe()


# In[130]:


#sum of all null values:
data.isnull().sum()


# In[131]:


#graph:
plt.hist(data.BasePay)
plt.show()


# In[132]:


plt.hist(data.OvertimePay)
plt.show()


# In[133]:


plt.hist(data.OtherPay)
plt.show()


# In[134]:


plt.hist(data.TotalPay)
plt.show()


# In[ ]:




