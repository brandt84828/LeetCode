#1
class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        fre = len(words)
        m = {}
        for word in words:
            for w in word:
                if w not in m:
                    m[w] = 1
                else:
                    m[w] += 1
        
        for v in m.values():
            if v % fre != 0:
                return False

        return True

#2
class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        joint = ''.join(words)
        set1 = set(joint)
        
        for i in set1 :
            if joint.count(i) % len(words) != 0 : return False 
        return True