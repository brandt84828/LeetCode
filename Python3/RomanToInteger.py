class Solution:
    def romanToInt(self, s: str) -> int:

        roman = {"M":1000, "D":500, "C":100, "L":50, "X":10, "V":5, "I":1}
        ans = 0

        for i in range(len(s)-1):
            if s[i]=="I" and (s[i+1]=="V" or s[i+1]=="X"):
                ans = ans - 1
            elif s[i]=="X" and (s[i+1]=="L" or s[i+1]=="C"):
                ans = ans - 10
            elif s[i]=="C" and (s[i+1]=="D" or s[i+1]=="M"):
                ans = ans - 100
            else:
                ans = ans + roman[s[i]]

        ans = ans + roman[s[-1]]

        return ans