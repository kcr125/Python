#!/usr/bin/env python
# coding: utf-8

# In[1]:


def read_single_digit(num) :
    if num == '0':
        return '영'
    if num == '1':
        return '일'
    if num == '2':
        return '이'
    if num == '3':
        return '삼'
    if num == '4':
        return '사'
    if num == '5':
        return '오'
    if num == '6':
        return '육'
    if num == '7':
        return '칠'
    if num == '8':
        return '팔'
    if num == '9' :
        return '구'
        
def read_number() :
    a = read_single_digit(num1)
    b = read_single_digit(num2)
    c = read_single_digit(num3)
    return a, b, c
    


number = input('세 자리 정수 입력:')
num1 = number[0]
num2 = number[1]
num3 = number[2]

print(read_number())


# In[ ]:




