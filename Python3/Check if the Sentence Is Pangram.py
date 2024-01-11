#1
class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        c = {}
        for s in sentence:
            if s in c:
                pass
            else:
                c[s] = 1
        
        return len(c) == 26

#2
class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        return len(set(sentence)) == 26