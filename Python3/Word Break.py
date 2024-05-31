#1
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        def construct(current,wordDict, memo={}):
            if current in memo:
                return memo[current]

            if not current:
                return True

            for word in wordDict:
                if current.startswith(word):
                    new_current = current[len(word):]
                    if construct(new_current,wordDict,memo):
                        memo[current] = True
                        return True

            memo[current] = False
            return False

        return construct(s,wordDict)

#2
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False for i in range(n+1)]
        dp[0] = True

        for i in range(1, len(s)+1):
            for w in wordDict:
                if i - len(w) >= 0 and dp[i - len(w)] and s[i - len(w):i] == w:
                    dp[i] = True
                
        return dp[-1]