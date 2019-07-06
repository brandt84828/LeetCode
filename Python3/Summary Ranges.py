# -*- coding: utf-8 -*-
"""
Created on Tue Sep 11 14:49:50 2018

@author: brand
"""

start = 0
end = 0

nums = [0,2,3,4,6,8,9]
ans = []

for i in range(0,len(nums)):
    if i == len(nums)-1:
        if start == end:
            ans.append(str(nums[i]))
        else:
            ans.append(str(nums[start])+"->"+str(nums[end]))
    elif nums[i]+1 == nums[i+1]:
        end = end + 1
    else:
        if start == end:    
            ans.append(str(nums[i]))
            start = start + 1
            end = start
        else:
            ans.append(str(nums[start])+"->"+str(nums[end]))
            end = end + 1
            start = end
            
ans

        