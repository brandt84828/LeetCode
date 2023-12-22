class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        n = len(s)
        count = 0

        for i in range(n-1,-1,-1):
            if count==0 and s[i] == ' ':
                continue
            else:
                if s[i] == ' ':
                    break
            count = count + 1
        return count