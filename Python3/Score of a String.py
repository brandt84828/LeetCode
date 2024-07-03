class Solution:
    def scoreOfString(self, s: str) -> int:
        res = 0
        for i in range(len(s)-1):
            temp = abs(ord(s[i]) - ord(s[i+1]))
            res += temp
        return res