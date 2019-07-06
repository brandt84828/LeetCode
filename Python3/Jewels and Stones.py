# -*- coding: utf-8 -*-
"""
Created on Thu Aug 16 11:03:42 2018

@author: brandt84828
"""

S='aAAbbbb'
J='aA'
#法一  較快 
sum([i in J for i in S])


#法二
count = 0
for i in range(0,len(J)):
    count = count + S.count(J[i])
    
print(count)