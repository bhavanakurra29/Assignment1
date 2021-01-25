#!/usr/bin/env python
# coding: utf-8

# # Question 1

# In[1]:


# Write a python program to print all prime numbers in an interval


# In[4]:


for m in range (1,37):
    if m>1:
        for n in range (2,m):
            if m%n==0:
                break
        else:
            print (m)


# # Question 2

# In[5]:


# Write a python program for factorial of a number.


# In[7]:


n=int(input("enter a value: "))
fact=1
for m in range (1,n+1):
    fact=fact*m
print(fact)
    


# # Question 3

# In[8]:


# find the sum of n numbers by using the while loop


# In[9]:


n=int(input("enter a value: "))
sum=0
for m in range (1,n+1):
    sum=sum+m
print(sum)


# In[ ]:




