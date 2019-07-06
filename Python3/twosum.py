# -*- coding: utf-8 -*-
"""
Created on Mon Aug 13 19:57:09 2018

@author: brandt84828
"""

nums = [3,3]
target = 6

#def twosums(nums,target):
num_dict ={}
ans=[]
for index,content in enumerate(nums):
    num_dict[content] = index
    

for i in range(0,len(nums)):
    temp = target - nums[i]
    if temp in num_dict and i != num_dict[temp]:
        print(i,num_dict[temp])
        break
        
    
     
#brute-force

nums = [3,2,4]
target = 6
        
for i in range(0,len(nums)):
    for j in range(i+1,len(nums)):
        if nums[i]+nums[j] == target:
            print(i,j)