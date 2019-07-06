# -*- coding: utf-8 -*-
"""
Created on Wed Aug 15 15:58:18 2018

@author: brandt84828
"""


class Solution:
    def isPalindrome(self, number):
        """
        :type x: int
        :rtype: bool
        """
        reverse = 0

        ori_number = number
        reverse = 0

        while(number>0):
            remainder = number % 10
            number = number // 10
            reverse = reverse*10+remainder


        if reverse == ori_number:
            return True
        else:
            return False