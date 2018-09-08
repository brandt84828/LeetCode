# -*- coding: utf-8 -*-
"""
Created on Thu Aug 23 13:57:55 2018

@author: brandt84828
"""

class Solution:
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        
        a = 0
        b = 0
        h1 = {}
        h2 = {}
        for idx in range(len(secret)):
            if secret[idx] == guess[idx]:
                a+=1
            else:#這樣最後不用扣A的次數
                if h1.get(secret[idx],None) != None:#get 沒有則回傳None
                    h1[secret[idx]]+=1
                else:
                    h1[secret[idx]]=1
                if h2.get(guess[idx],None) != None:
                    h2[guess[idx]]+=1
                else:
                    h2[guess[idx]]=1
        for key in h1:
            if h2.get(key,None) != None:
                b += min(h1[key],h2[key])
        return str(a) + 'A' + str(b) + 'B'


#2 可以利用collection 的counter套件直接算出total 再回去-A 得出B
from collections import Counter

secret = Counter('1123')
guess = Counter('0111')

Total = secret & guess #交集

#接著算出A 再用Total - A >> B