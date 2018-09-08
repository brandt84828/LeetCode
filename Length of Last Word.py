# -*- coding: utf-8 -*-
"""
Created on Tue Aug 21 11:01:02 2018

@author: brandt84828
"""



#Use in build function ,split
if len(s) == 0:
    return 0
s = s.rstrip(' ').split(' ')[-1]
return len(s)
    
    


s = "a "
count = 0
pre = 0
for i in s:
    if i == ' ':
        pre = count
        count = 0
    else:
        count = count + 1
    
if count == 0:
    print(pre)
else:
    print(count)