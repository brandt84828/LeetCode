#1
class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        ma = 0
        for s in sentences:
            sp = s.split(" ")
            ma = max(ma, len(sp))

        return ma
        

#2
class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        return max(s.count(" ") for s in sentences) + 1
        