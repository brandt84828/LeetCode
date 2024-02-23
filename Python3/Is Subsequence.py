#1
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) > len(t):return False
        if len(s) == 0:return True
        subsequence=0
        for i in range(0,len(t)):
            if subsequence <= len(s) -1:
                if s[subsequence]==t[i]:

                    subsequence+=1
        return  subsequence == len(s) 
#2
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        remainder_of_t = iter(t)
        for letter in s:
            if letter not in remainder_of_t:
                return False
        return True

#3
class Solution:
    def isSubsequence(self, s, t):
        s_i, t_i = 0, 0
        
        while s_i < len(s) and t_i < len(t):
            s_i, t_i = s_i + (s[s_i] == t[t_i]), t_i + 1
            
        return s_i == len(s)