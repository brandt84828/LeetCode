# -*- coding: utf-8 -*-
"""
Created on Sun Aug 19 14:49:10 2018

@author: brandt84828
"""

nums =[1,2,3,4]

#套用數學公式 
expected_sum = len(nums)*(len(nums)+1)//2
actual_sum = sum(nums)

if min(nums) != 0 :
    return 0
elif expected_sum==actual_sum:
    return max(nums)+1
else:
    return expected_sum-actual_sum