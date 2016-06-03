
# coding: utf-8

# In[1]:

from fuzzywuzzy import fuzz
from fuzzywuzzy import process
import re
import pandas as pd


# In[2]:

mydata = pd.read_excel("Book1.xlsx",sheetname= "Sheet1")


# In[3]:

del mydata['Unnamed: 3']


# In[4]:

mydata.head(1)


# In[5]:

mymargins = mydata[[0,1,2]]


# In[6]:

mymargins = mymargins.dropna()


# In[7]:

mymargins.head(1)


# In[8]:

myflowers = mydata[[3,4,5]]


# In[9]:

myflowers.head(1)


# In[15]:

choices = {mymargins['Row Labels'].iloc[i] : mymargins['Margin %'].iloc[i] for i in range(mymargins.shape[0])}
def matching (x):
    x = str(x)
    return choices[process.extractOne(x, choices.keys())[0]] 
#,str(choices[y[0]]),str(y[1])


# In[19]:

myflowers['discount'] = myflowers["Cost Centre Description"].apply(lambda x: matching(x))


# In[21]:

myflowers.head(1)


# In[25]:

myflowers.to_excel("output.xlsx",index=None)


# In[16]:

get_ipython().magic('pinfo myflowers.apply')


# In[ ]:



