# -*- coding: utf-8 -*-
"""
Created on Wed Aug 15 19:58:04 2018

@author: brandt84828
"""

a = 'A man, a plan, a canal: Panama'

result=''

for i in range(len(a)-1,-1,-1):
    result = result + a[i]
    
    
print(result)



#Also can use a[::-1] , very simple