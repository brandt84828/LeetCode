# -*- coding: utf-8 -*-
"""
Created on Sat Sep 15 13:53:06 2018

@author: brand
"""

moves = 'RL'
x=0;y=0

for char in moves:
    if char == 'U':
        y = y + 1
    elif char =='D':
        y = y - 1
    elif char == 'L':
        x = x + 1
    elif char == 'R':
        x = x- 1
        
if x==0 and y==0:
    print('True')
else:
    print('False')