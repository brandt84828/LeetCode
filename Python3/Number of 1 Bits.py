# -*- coding: utf-8 -*-
"""
Created on Sun Aug 19 20:52:29 2018

@author: brandt84828
"""


#內建函數寫法
n = 11
bin(n).count("1")     


#利用and 運算
class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        while n > 0:
            count += (n & 1)
            n >>= 1
        return count