#!/usr/bin/env python
# coding: utf-8

# Example notebook to plot boolean state values using matplotlib.axes.Axes.pcolormesh
# 
# https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.pcolormesh.html

# In[8]:


import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import numpy as np
from random import randrange

# optional for interactive plot
get_ipython().run_line_magic('matplotlib', 'widget')


# In[9]:


# make fake data, np boolean type
xm, ym = 40, 16
boo = np.eye(ym, M=xm, dtype=bool)    # ones on the diagonal

for i in range(20):    # add some random points
    boo[randrange(ym), randrange(xm)] = True

# print('boo shape', boo.shape)


# In[10]:


# Prepare array for plotting, data in even rows, zeros (false) in odd rows.
# Blank rows add whitespace in the image plot.

boo2shape = (boo.shape[0] * 2 , boo.shape[1])    # shape of new array
boo2 = np.zeros(boo2shape, dtype=boo.dtype)      # new array, all false, same type as boo

boo2[0::2] = boo    # copy existing data into even rows of new array


# See https://stackoverflow.com/questions/5347065/interleaving-two-numpy-arrays-efficiently for array method.

# In[11]:


# tick and label setup
ytp = np.arange(0, boo2.shape[0], 2) + 0.5   # y tick positions with offset
ytl = np.arange(boo.shape[0])                # y tick labels (numeric)
xtp = np.arange(boo2.shape[1]) + 0.5         # x tick positions with offset
xtl = np.arange(boo2.shape[1])               # x tick labels (numeric)

wht_blue = ListedColormap(['White', 'Royalblue'])    # discrete colormap

# make plot using pcolormesh
fig, ax1 = plt.subplots(figsize=(12, 5))
ax1.pcolormesh(boo2, cmap=wht_blue)
ax1.grid(color='lightgray')
ax1.set_yticks(ytp, ytl)
ax1.set_ylabel('channel')
ax1.set_xticks(xtp, xtl)
ax1.set_xlabel('cycle')
plt.show()


# In[12]:


# negate the array for a different plot
boo = np.logical_not(boo)


# In[13]:


# Prepare array for plotting, data in even rows, zeros (false) in odd rows.
# Rows of zero add whitespace in the image plot.

boo2shape = (boo.shape[0] * 2 , boo.shape[1])    # shape of new array
boo2 = np.zeros(boo2shape, dtype=boo.dtype)      # new array, all false, same type as boo

boo2[0::2] = boo    # copy existing data into even rows of new array


# In[14]:


# tick and label setup
ytp = np.arange(0, boo2.shape[0], 2) + 0.5   # y tick positions with offset
ytl = np.arange(boo.shape[0])                # y tick labels (numeric)
xtp = np.arange(boo2.shape[1]) + 0.5         # x tick positions with offset
xtl = np.arange(boo2.shape[1])               # x tick labels (numeric)

wht_blue = ListedColormap(['White', 'Royalblue'])    # discrete colormap

# make plot using pcolormesh
fig, ax1 = plt.subplots(figsize=(12, 5))
ax1.pcolormesh(boo2, cmap=wht_blue)
ax1.grid(color='lightgray')
ax1.set_yticks(ytp, ytl)
ax1.set_ylabel('channel')
ax1.set_xticks(xtp, xtl)
ax1.set_xlabel('cycle')
plt.show()


# In[ ]:




