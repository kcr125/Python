#!/usr/bin/env python
# coding: utf-8

# In[4]:


def get_fixed_price(count) :  
    return count / (100-dis) *100

dis = int(input('할인율은? '))
cou1 = int(input('A 상품의 할인된 가격은? '))
cou2 = int(input('B 상품의 할인된 가격은? '))

print('A 상품의 정가는', get_fixed_price(cou1),'원')
print('B 상품의 정가는', get_fixed_price(cou2),'원')


# In[ ]:




