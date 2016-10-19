
# coding: utf-8

# In[23]:

import numpy as np
import pandas as pd


# In[24]:

from numpy.random import randn


# In[25]:

np.random.seed(101)


# In[26]:

df=pd.DataFrame(randn(5,4),['A','B','C','D','E'],['W','X','Y','Z'])


# In[27]:

df


# In[28]:

df['W']


# In[29]:

df.W


# In[30]:

df[['W','Z']]


# In[33]:

df['new'] = df['W']+df['Y']


# In[35]:

df


# In[38]:

df.drop('new',axis=1,inplace=True)


# In[39]:

df


# In[40]:

df.drop('E')


# In[41]:

df


# In[43]:

df.loc['A']


# In[44]:

df.iloc[2]


# In[45]:

df.loc['B','Y']


# In[46]:

df > 0


# In[47]:

df[df>0]


# In[48]:

df


# In[49]:

df['W']>0


# In[50]:

df[df['W']>0]


# In[51]:

df[(df['W']>0) & (df['Y']>1)]


# In[52]:

df.reset_index()


# In[54]:

newind = 'CA NY WY RO CO'.split()


# In[55]:

df['States'] = newind


# In[56]:

df


# In[57]:

df.set_index('States')


# In[ ]:



