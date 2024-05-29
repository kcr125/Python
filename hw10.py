#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pickle
import os
input_list =[]

def input_scores() :
    i = 1
    while True :
        n = int(input(f'#{i}? '))
        if n < 0:
            break

        input_list.append(n)
        i += 1
        
    return input_list

def get_average(l) :
    a = sum(l)/len(l)
    return a

def show_scores() :
    print('[점수 출력]')
    print('개인점수:', *input_list)
    print('평균:', get_average(input_list))
    
def save_data():
    with open(filepath, 'wb') as file:
        pickle.dump(input_list, file)

def load_data():
    with open(filepath, 'rb') as file:
        data = pickle.load(file)
        return data
        

filepath = 'data/score.bin'

if os.path.exists(filepath):
    global input_list
    print('[파일 읽기]\n')
    input_list=load_data()
    show_scores()

else :
    print('[점수 입력]')
    input_scores()
    show_scores()
    save_data()


# In[ ]:




