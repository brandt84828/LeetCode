# -*- coding: utf-8 -*-
"""
Created on Sun Aug 19 14:07:05 2018

@author: brandt84828
"""
# 利用xor 消除重複的
nums = [2,2,1]
x = 0
for i in nums:
    x = x ^ i
    
print(x)

