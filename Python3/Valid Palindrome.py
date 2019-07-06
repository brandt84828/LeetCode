# -*- coding: utf-8 -*-
"""
Created on Thu Sep 13 19:33:52 2018

@author: brand
"""
class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        new = ''
        for item in s:
            if item.isalpha()==True or item.isnumeric()==True:#判斷是否為字符or數字
                new = new + item

        if new.lower() == new[::-1].lower():#都轉小寫
            return True
        else:
            return False