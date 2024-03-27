#!/usr/bin/env python
# coding: utf-8

# In[1]:


def exchange(change) :
    a1=change//500
    a2=change%500
    b1=a2//100
    b2=a2%100
    c1=b2//50
    c2=b2%50
    d1=c2//10
    print('500원 동전의 개수:', a1)
    print('100원 동전의 개수:', b1)
    print('50원 동전의 개수:', c1)
    print('10원 동전의 개수:', d1)
    
def get_integer(prompt) :
    res=int(input(prompt))
    return res

change=get_integer('동전으로 교환하고자 하는 금액은?')
exchange(change)


# In[ ]:




