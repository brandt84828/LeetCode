# -*- coding: utf-8 -*-
"""
Created on Sat Aug 18 09:45:09 2018

@author: brandt84828
"""
s = "pwwkew"
start,end =0,0
used=''
max_n = 0
for i in range(0,len(s)):
    end = end + 1
    if s[i] in used:
        start = s.index(s[i],start) + 1#防止index不動一直取第一個重複
    used = s[start:end]
    if len(used)>max_n:#找出最大的length
        max_n = len(used)
    print(i,s[i],used,start,end)

print(max_n)