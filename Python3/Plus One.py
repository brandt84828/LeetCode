# -*- coding: utf-8 -*-
"""
Created on Sun Aug 19 11:25:52 2018

@author: brandt84828
"""

digits = [1,2,9,9]


    
for i in range(len(digits)-1,-1,-1):
    digits[i]=digits[i]+1
    if digits[i]==10:
        digits[i]=0
        if digits[0]==0:
            digits.insert(0,1)
        continue
    else:
        break
print(digits)