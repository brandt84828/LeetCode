# -*- coding: utf-8 -*-
"""
Created on Thu Aug 16 13:55:35 2018

@author: brandt84828
"""

s = "IV"
roman = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
total = 0


for i in range(0,len(s)-1):
    if s[i] =='I' and (s[i+1]=='V' or s[i+1]=='X'):
        total = total - 1
    elif s[i] =='X' and (s[i+1]=='L' or s[i+1]=='C'):
        total = total - 10
    elif s[i] =='C' and (s[i+1]=='D' or s[i+1]=='M'):
        total = total - 100
    else:
        total = total + roman[s[i]]

total = total + roman[s[-1]]


print(total)