# -*- coding: utf-8 -*-
"""
Created on Wed Aug  8 13:30:29 2018

@author: brandt84828
"""


for i in range(1,101):
    if i % 3 == 0 and i% 5 ==0:
        print('fizzbuzz')
    elif i % 3 ==0:
        print('fizz')
    elif i % 5 ==0:
        print('buzz')
    else:
        print(i)
        
        
        