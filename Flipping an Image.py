# -*- coding: utf-8 -*-
"""
Created on Sat Sep 15 15:43:39 2018

@author: brand
"""

A = [[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]
B = []
for i in A:
    B.append(i[::-1])
    
for i in range(0,len(B)):
    for j in range(0,len(B[i])):
        B[i][j] = B[i][j] ^ 1
        
B
        