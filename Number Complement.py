# -*- coding: utf-8 -*-
"""
Created on Mon Aug 20 13:30:56 2018

@author: brandt84828
"""

n = 1


a=bin(n)[2:]
b=''
for i in range(0,len(a)):
    b = b + str(int(a[i]) ^ 1)
    
    
int(b,2)