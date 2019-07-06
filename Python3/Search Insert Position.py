# -*- coding: utf-8 -*-
"""
Created on Thu Aug 16 15:43:40 2018

@author: brandt84828
"""

nums = [1,3,5,6]
target = 7

index = len(nums)

for i in range(0,len(nums)):
    if nums[i]>target:
        index = i
        break
    elif nums[i]<target:
        pass
    else:
        index = i
        break

        
print(index)



#較快 加進去直接取index
sorted(nums + [target]).index(target)