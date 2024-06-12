#1
class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        i = 0
        for c in s:
            if i < len(t) and c == t[i]:
                i = i + 1
        
        return len(t) - i

#2
class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        s_index, t_index = 0, 0
        s_length, t_length = len(s), len(t)
    
        while s_index < s_length and t_index < t_length:
            if s[s_index] == t[t_index]:
                t_index += 1
            s_index += 1
    
        return t_length - t_index