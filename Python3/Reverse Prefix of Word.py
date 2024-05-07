#1
class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        index = 0
        for i in range(len(word)):
            if word[i] == ch:
                index = i
                break
        
        return word[:index+1][::-1] + word[index+1:]

#2
class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        temp = []
        res = ""
        index = 0
        for i in range(len(word)):
            temp.append(word[i])
            if word[i] == ch:
                index = i
                break


        for i in range(index,-1,-1):
            res += temp[i]

        for i in range(index+1, len(word)):
            res += word[i]

        return res

#3
class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        idx=word.find(ch)    
        if idx:
            return word[:idx+1][::-1]+ word[idx+1:]
        return word