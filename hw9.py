#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Rectangle:
    def __init__(self, x1=0, y1=0, x2=0, y2=0):
        self.__x1=x1
        self.__y1=y1
        self.__x2=x2
        self.__y2=y2
        
    def show(self):
        print(f'좌측 상단 꼭짓점이 ({self.__x1}, {self.__y1})이고 우측 하단 꼭짓점이 ({self.__x2}, {self.__y2})인 사각형입니다.')

    def getWidth(self):
        return self.__x2 - self.__x1

    def getHeight(self):
        return self.__y2 - self.__y1
        
    @staticmethod
    def getArea():
        return r1.getWidth() * r1.getHeight()

    @staticmethod
    def getPerimeter():
        return (r1.getWidth() + r1.getHeight()) * 2
    

r1 = Rectangle(5, 5, 20, 10)
a = r1.getArea()
p = r1.getPerimeter()

r1.show()
print(f'넓이는 {a}, 둘레는 {p}')


# In[ ]:




