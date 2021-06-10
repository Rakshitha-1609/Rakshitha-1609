#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Even Case
x = input("Enter your input: ")
print('Length of your string is', len(x))
if (len(x) % 2 == 0):
    print("Length of your string is Even")
else:
    print("Length of your string is Odd")
def middle_char(x):
    return x[(len(x)-1)//2:(len(x)+2)//2]
print("Middle character of your string is", middle_char(x))


# In[2]:


#Odd Case
x = input("Enter your input: ")
print('Length of your string is', len(x))
if (len(x) % 2 == 0):
    print("Length of your string is Even")
else:
    print("Length of your string is Odd")
def middle_char(x):
    return x[(len(x)-1)//2:(len(x)+2)//2]
print("Middle character of your string is", middle_char(x))


# In[ ]:




