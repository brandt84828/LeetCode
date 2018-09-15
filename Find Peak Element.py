# -*- coding: utf-8 -*-
"""
Created on Sat Sep 15 14:31:41 2018

@author: brand
"""

nums = [1,2,1,3,5,6,4]
class Solution:
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return 0
        elif len(nums) == 2:
            if nums[1]>nums[0]:
                return 1
            else:
                return 0
        else:
            if nums[0]>nums[1]:
                ans = 0
            elif nums[-1]>nums[-2]:
                ans = len(nums)
            for i in range(1,len(nums)-1):
                if nums[i-1]<nums[i] and nums[i]>nums[i+1]:
                    ans = i
                    break
            return ans