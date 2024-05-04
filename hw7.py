#!/usr/bin/env python
# coding: utf-8

# In[1]:


shopping_bag = {}

print('[구입]')
while True :
    item = input('상품명?')
    if (item == '') :
        break
    amount = input('수량은?')
    shopping_bag[item] = amount
    print(f'장바구니에 {item} {amount}개가 담겼습니다.\n')
   
print('\n>>>장바구니 보기:',shopping_bag)

print('\n[검색]')
search = input('장바구니에서 확인하고자 하는 상품은?')
print(f'{search}은(는) {shopping_bag.get(search)}개가 담겨 있습니다.')


# In[ ]:




