# -*- coding: utf-8 -*-
"""
Created on Sun Aug 19 16:45:37 2018

@author: brandt84828
"""

s = "abcd"
t = "aabcd"

def test(s,t):
    for i in t:
        if t.count(i) != s.count(i):
            return i
test(s,t)
    



#利用xor 快!    
def findTheDifference(self, s, t):
    """
    :type s: str
    :type t: str
    :rtype: str
    """
    ans = 0
    for c in s + t:
        ans ^= ord(c)
    return chr(ans)