# -*- coding: utf-8 -*-
"""
Created on Mon Aug 20 11:08:49 2018

@author: brandt84828
"""

n = 4

class Solution(object):
def isPowerOfTwo(self, n):
    """
    :type n: int
    :rtype: bool
    """
    if n <= 0:
        return False
    
    while(n%2==0):
        n = n//2
    if n == 1:
        return True
    else:
        return False
