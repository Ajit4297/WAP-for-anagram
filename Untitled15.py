#!/usr/bin/env python
# coding: utf-8

# In[14]:


s = input() # mmrrtte
ss='abcdefghijklmnopqrstuvwxyz'
flag=True
for i in ss:
    if i not in s:
        flag=False
        break
print('yes' if flag else 'no')    


# In[ ]:




