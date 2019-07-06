# -*- coding: utf-8 -*-
"""
Created on Sat Aug 18 13:02:23 2018

@author: brandt84828
"""
#法一 時間花費高
x = 1
error = 1
index = x
for i in range(1,x):
    error = x-i**2
    if error>=0:        
        index = i
    else:
        break

    
print(index)



#法二python最快寫法

return x**0.5


#Binary Search

def binary(x):
    if x == 0:
        return 0
    if x == 1:
        return 1 
    left = 2
    right = x
    while left < right:
        middle = (left + right) // 2
        mid_squared = middle*middle
        if mid_squared == x:
            return middle
        elif mid_squared < x:
            left = middle + 1
        else:
            right = middle - 1
    return left-1 if left*left > x else left 

binary(6)


