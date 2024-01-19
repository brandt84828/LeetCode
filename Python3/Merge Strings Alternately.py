#1
class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        result = []
        i = 0
        while i < len(word1) or i < len(word2):
            if i < len(word1):
                result.append(word1[i])
            if i < len(word2):
                result.append(word2[i])
            i += 1
        return ''.join(result)

#2
class Solution(object):
    def mergeAlternately(self, word1, word2):
        result = []
        for i in range(min(len(word1),len(word2))):
            result.append(word1[i] + word2[i])
            
        return ''.join(result) + word1[i+1:] + word2[i+1:]