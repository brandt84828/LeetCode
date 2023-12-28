#1
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        if len(ransomNote) > len(magazine):
            return False

        table = [0] * 26

        for c in magazine:
            table[ord(c)-97] = table[ord(c)-97] + 1
        for c in ransomNote:
            table[ord(c)-97] = table[ord(c)-97] - 1
            if table[ord(c)-97] < 0:
                return False
        return True

#2
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        return not collections.Counter(ransomNote) - collections.Counter(magazine)