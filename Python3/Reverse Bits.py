# -*- coding: utf-8 -*-
"""
Created on Mon Aug 20 10:43:03 2018

@author: brandt84828
"""

n = 43261596
#Problem request 32 bits,so zfill(32)
#zfill 前面會補0至該位數
reverse = bin(n)[2:].zfill(32)[::-1]

print(reverse)

#another way
class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
            r = 0
            for i in range(32):
                r <<= 1
                r |= n & 1
                n >>= 1
            return r