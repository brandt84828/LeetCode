#1
class Solution:
    def repeatedCharacter(self, s: str) -> str:
        m = {}
        for i, v in enumerate(s):
            if  v in m:
                return v  
            else:
                m[v] = 1

#2
class Solution:
    def repeatedCharacter(self, s: str) -> str:
        vis = set()
        for i in s:
            if i in vis:
                return i 
            else:
                vis.add(i)
        