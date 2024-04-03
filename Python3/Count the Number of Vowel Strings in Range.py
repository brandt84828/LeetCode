#1
class Solution:
    def vowelStrings(self, words: List[str], left: int, right: int) -> int:
        m = ["a", "e", "i", "o", "u"]
        res = 0
        for i in range(left, right + 1):
            if words[i][0] in m and words[i][-1] in m:
                res+=1
        
        return res

#2
class Solution:
    def vowelStrings(self, words: List[str], left: int, right: int) -> int:
        vowels = set('aeiou')
        
        return sum({w[0],w[-1]}.issubset(vowels) for w in words[left:right+1])