#!/usr/bin/env python
# coding: utf-8

# In[131]:


from sklearn.datasets import make_classification
import numpy as np
import pandas as pd
import os
import matplotlib
#%matplotlib inline
import matplotlib.pyplot as plt
import seaborn as sns


# In[132]:


dataset = pd.read_csv("results.csv")
dataset.head()


# In[133]:


dataset['position'] = dataset['position'].fillna(0)


# In[134]:


y = dataset['position']


# In[136]:


dataset=dataset.drop(dataset.columns[3], axis=1)
dataset.head()


# In[137]:


X=dataset.drop(dataset.columns[2], axis=1)


# In[138]:


X.head()


# In[139]:


y.head()


# In[140]:


from sklearn.preprocessing import StandardScaler
from sklearn import preprocessing


# In[141]:


names = X.columns


# In[142]:


scaler = preprocessing.StandardScaler()
# Fit your data on the scaler object
X_scaled = scaler.fit_transform(X)
X_scaled = pd.DataFrame(X_scaled, columns=names)
X_before=X
y_before=y
X_after=X_scaled
y_after=y


# In[144]:


from sklearn import preprocessing
from sklearn.model_selection import cross_validate
from sklearn.model_selection import cross_val_score
from sklearn import svm
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X_after, y_after, test_size=0.2, random_state=0)
model=SVC(kernel='rbf', probability=True)
model.fit(X_before, y_before)


# In[67]:


import pickle


# In[68]:


filename = 'ML_model.sav'
pickle.dump(model, open(filename, 'wb'))


# In[69]:


loaded_model = pickle.load(open(filename, 'rb'))
result = loaded_model.score(X_test, Y_test)
print(result)


# In[145]:


X_new = pd.read_csv("X_new.csv")
X_new.head()


# In[146]:


Y_new = model.predict_proba(X_new)


# In[161]:


for i in range(len(X_new)):
    print(np.max(Y_new[i]))


# In[ ]:




