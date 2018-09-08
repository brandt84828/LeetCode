# -*- coding: utf-8 -*-
"""
Created on Thu Aug 23 10:18:48 2018

@author: brandt84828
"""

A = "" 
B = ""

List_A = A.split(' ')
List_B = B.split(' ')

Total = List_A + List_B

ans=[]
for i in range(0,len(Total)):
    if Total[i]=='':
        continue
    if Total.count(Total[i])==1:
        ans.append(Total[i])
    
        
        
ans