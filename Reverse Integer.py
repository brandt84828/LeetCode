# -*- coding: utf-8 -*-
"""
Created on Wed Aug 15 14:05:35 2018

@author: brandt84828
"""
class Solution:
    def reverse(self, number):
        """
        :type x: int
        :rtype: int
        """
        result = 0
        sign = True
        if number < 0:
            sign = False
            number = abs(number)

        while(number>0):
            remainder = number % 10
            number = number // 10

            result = result*10+remainder

        if sign == False:
            result = result*-1

        if -2**31 <= result <= 2**31-1:
            return result
        else:
            return 0