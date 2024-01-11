#1
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        r = {"b":0, "a":0, "l":0, "o":0, "n":0}
        for s in text:
            if s in r:
                r[s] = r[s] + 1
        
        ans = 10000

        for k, v in r.items():
            if k == "l" or k == "o":
                ans = min(ans, v // 2)
            else:
                ans = min(ans, v)
        
        return ans

#2
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        count = {"b": 0, "a": 0, "l": 0, "o": 0, "n":0}
        
        for i in text:
            if i in count:
                count[i] += 1
        
        count["l"] = count["l"] // 2
        count["o"] = count["o"] // 2
        
        return min(count.values())