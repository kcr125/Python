#!/usr/bin/env python
# coding: utf-8

# In[1]:


def buy(shopping_bag):
    print('[구입]')
    item = input('상품명?')
    if (item == ''):
        return False
    amount = int(input('수량은?'))
    shopping_bag[item] = amount
    print(f'장바구니에 {item} {amount}개가 담겼습니다.\n')
    
def show(shopping_bag):
    print('\n>>>장바구니 보기:',shopping_bag)
    
def find(lst):
    print('\n[검색]')
    n = input('장바구니에서 확인하고자 하는 상품은?')
    if n in lst :
        print(f'{n}은(는) {shopping_bag[n]}개가 담겨 있습니다.')   
    else :
        print(f'장바구니에 {n}은(는) 없습니다.')   


shopping_bag = {}
while True :
    if buy(shopping_bag) == False:         #리턴값을 받아야 false를 인지?
        break
show(shopping_bag)
find(shopping_bag)


# In[ ]:




