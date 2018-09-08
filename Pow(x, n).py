# -*- coding: utf-8 -*-
"""
Created on Thu Aug 16 14:56:05 2018

@author: brandt84828
"""


def pow(x,n):
    ans=1

    if n > 0 :
        ans = ans*pow(x,n-1)*x
    elif n < 0 :
        ans = ans/x*pow(x,n+1)
    else:
        ans=1
        
    return ans
        
        
        
pow(2.10000,3)
        
