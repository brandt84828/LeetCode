# -*- coding: utf-8 -*-
"""
Created on Wed Aug 15 20:37:43 2018

@author: brandt84828
"""

   
nums = [1,4,3,2]

nums.sort()
ans = 0
for i in range(0,len(nums),2):
    ans = ans + nums[i]
    
    
print(ans)
    
#最簡便 return sum(sorted(nums)[::2]) 

class Solution:
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        ans = 0
        for i in range(0,len(nums),2):
            ans = ans + min(nums[i],nums[i+1])
            
        return ans