#1
class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        result = []
        for word in words:
            for i in words:
                if word in i and word != i:
                    result.append(word)
                    break
        return result

#2
class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        arr = ' '.join(words)
        subStr = [i for i in words if arr.count(i) >= 2]
                
        return subStr