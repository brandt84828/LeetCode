# -*- coding: utf-8 -*-
"""
Created on Thu Sep 13 20:01:49 2018

@author: brand
"""

class Solution(object):
    def twoSum(self, numbers, target):
        m = {}
        for i in range(len(numbers)):
            n = numbers[i]
            comp = target - n
            if comp in m:
                return m[comp] + 1, i + 1
            m[n] = i
        return None
    
#在一堆重複的答案會和題目不相同