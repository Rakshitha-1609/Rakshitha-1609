#!/usr/bin/env python
# coding: utf-8

# In[1]:


def common(p, q):
    flag = False
    for i in p:
        if (i in q):
            flag = True
        else:
            pass
    return flag

p = [10, 11, 12, 13, 14]
q = [14, 15, 16, 17, 18]
result = common(p, q)
print('The above lists have at least one common member:',result)


# In[ ]:




