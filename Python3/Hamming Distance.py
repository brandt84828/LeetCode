# -*- coding: utf-8 -*-
"""
Created on Thu Aug 16 11:19:30 2018

@author: brandt84828
"""

x=1
y=4

z = x ^ y

#40ms
bin(z).count('1')


#較快36ms

sum([int(i) for i in bin(z) if i=='1'])
    