#1
class Solution:
    def maxScore(self, s: str) -> int:
        zeros = 1 if s[0] == '0' else 0
        ones = s.count('1', 1)  # count 1s in s[1:]
        score = zeros + ones
        for i in range(1, len(s) - 1):
            if s[i] == '0':
                zeros += 1
            else:
                ones -= 1
            score = max(zeros + ones,  score)
        return score

#2
class Solution:
    def maxScore(self, s: str) -> int:
        ones = 0
        zeros = 0
        best = -inf

        for i in range(len(s) - 1):
            if s[i] == "1":
                ones += 1
            else:
                zeros += 1
            
            best = max(best, zeros - ones)
            
        if s[-1] == "1":
            ones += 1
        
        return best + ones