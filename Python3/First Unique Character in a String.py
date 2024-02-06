#1
class Solution:
    def firstUniqChar(self, s: str) -> int:
        m = {}
        res = -1
        for i in range(len(s)):
            if s[i] in m:
                m[s[i]] = m[s[i]] + 1
            else:
                m[s[i]] = 1

        for i in range(len(s)-1,-1,-1):
            if m[s[i]] == 1:
                res = i

        return res
            
            
#2
class Solution:
    def firstUniqChar(self, s):
        letters='abcdefghijklmnopqrstuvwxyz'
        index=[s.index(l) for l in letters if s.count(l) == 1]
        return min(index) if len(index) > 0 else -1
            
#3
class Solution:
    def firstUniqChar(self, s):
        d = {}
        seen = set()
        for idx, c in enumerate(s):
            if c not in seen:
                d[c] = idx
                seen.add(c)
            elif c in d:
                del d[c]
        return min(d.values()) if d else -1