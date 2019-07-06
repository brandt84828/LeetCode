# -*- coding: utf-8 -*-
"""
Created on Thu Aug 16 16:30:13 2018

@author: brandt84828
"""

s = ']'
stack=[]
try:#用try直接避免掉index out of range的問題 ， 直接拿stack[-1]充當top
    for i in s:
        if i ==')' and stack[-1]=='(':
            stack.pop()
        elif i ==']' and stack[-1]=='[':
            stack.pop()
        elif i =='}' and stack[-1]=='{':
            stack.pop()
        else:
            stack.append(i)
    if stack==[]:
        print(True)
    else:
        print(False)
    
except IndexError:
    print(False)

#利用字典 比較快    
class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        melt_dict = {')':'(', '}':'{', ']':'['}
        stack = [None]
        for p in s:
            if (p not in melt_dict) or (stack[-1] != melt_dict[p]): 
                stack.append(p)
            else: stack.pop()
        return len(stack) == 1