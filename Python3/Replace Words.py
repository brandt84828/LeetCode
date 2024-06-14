#1
class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        rootset = set(dictionary)

        def replace(word):
            for i in range(1, len(word)):
                if word[:i] in rootset:
                    return word[:i]
            return word

        return " ".join(map(replace, sentence.split()))

#2
class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        trie = {}
        
        for word in dictionary:
            t = trie
            for ch in word:
                if ch not in t:
                    t[ch] = {}
                t = t[ch]
            t['#'] = '#'

        def process(string):
            t = trie
            for i,ch in enumerate(string):
                if ch not in t:
                    break
                t = t[ch]
                if '#' in t:
                    return string[:i+1]
            return string
        
        return ' '.join(map(process, sentence.split()))