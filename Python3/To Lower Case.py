# -*- coding: utf-8 -*-
"""
Created on Wed Aug 15 19:10:55 2018

@author: brandt84828
"""

str = "al&phaBET"
result=''
char=''

for i in range(0,len(str)):
    if  90>=ord(str[i])>=65:
        char=chr(ord(str[i])+32)
    else:
        char = str[i]        
    result = result + char
    

print(result)