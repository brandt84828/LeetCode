# -*- coding: utf-8 -*-
"""
Created on Tue Sep 11 18:41:27 2018

@author: brand
"""

nums = [2,2]

total = len(nums)*(1+len(nums)) // 2
miss = total - sum(set(nums)) 
rep = sum(nums) - sum(set(nums)) 

ans = []
ans.append(rep)
ans.append(miss)

ans