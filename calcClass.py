#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class calculator():
    def __init__(self):
        self.x = int(input('Enter num1: '))
        self.y = int(input('Enter num2: '))
        print('1.add')
        print('2.sub')
        print('3.mul')
        print('4.div')
        z = int(input('Enter choice: '))
        if z == 1:
            self.add()
        elif z == 2:
            self.sub()
        elif z == 3:
            self.mul()
        elif z == 4:
            try:
                self.div()
            except:
                print('ZeroDivError')
        else:
            print('invalid option')
            
    def add(self):
        print(self.x + self.y)
    def sub(self):
        print(self.x - self.y)
    def mul(self):
        print(self.x * self.y)
    def div(self):
        print(self.x / self.y)

while True:
    ins_calc = calculator()


# In[ ]:





# In[ ]:




