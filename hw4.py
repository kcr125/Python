#!/usr/bin/env python
# coding: utf-8

# In[1]:


def rep_char(c, n) :
    print(c*n)

def draw_line_string(name):
    msg1 = 'Hello ' + name + ','
    msg2 = 'Welcome to Seoul.'
    
    if len(msg1) > len(msg2) : 
        nstr = len(msg1)
    else :  
        nstr = len(msg2)
        
    rep_char('-', nstr + 4 )
    print(f' {msg1} ')
    print(f' {msg2} ')
    rep_char('-', nstr + 4 )

                 
draw_line_string(input('Input his/her name:'))


# In[2]:


def rep_char(c, n) :
    print(c*n)

def draw_line_string(name):
    msg1 = 'Hello ' + name + ','
    msg2 = 'Welcome to Seoul.'
    
    if len(msg1) > len(msg2) : 
        nstr = len(msg1)
    else :  
        nstr = len(msg2)
        
    rep_char('-', nstr + 4 )
    print(f' {msg1} ')
    print(f' {msg2} ')
    rep_char('-', nstr + 4 )

                 
draw_line_string(input('Input his/her name:'))


# In[ ]:




