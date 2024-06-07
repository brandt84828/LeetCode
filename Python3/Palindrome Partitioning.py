#1
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        self.dfs(s, [], res)
        return res

    def dfs(self, s, path, res):
        if not s:
            res.append(path)
            return
        for i in range(1, len(s)+1):
            if self.isPal(s[:i]):
                self.dfs(s[i:], path+[s[:i]], res)
        
    def isPal(self, s):
        return s == s[::-1]

#2
class Solution:
    @cache  # the memory trick can save some time
    def partition(self, s: str) -> List[List[str]]:
        if not s: return [[]]
        ans = []
        for i in range(1, len(s) + 1):
            if s[:i] == s[:i][::-1]:  # prefix is a palindrome
                for suf in self.partition(s[i:]):  # process suffix recursively
                    ans.append([s[:i]] + suf)
        return ans

#3
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def find_all_palindromes(s):
            B = [0] * (2*n)
            for i, j in combinations_with_replacement(range(n), 2):
                if s[i:j+1] == s[i:j+1][::-1]:
                    B[i+j+1] = max(B[i+j+1], j-i+1)
            return B
        
        n = len(s)
        B = find_all_palindromes(s)
        
        dp = [[] for _ in range(n+1)]
        dp[0] = [[]]
        for i in range(0, n):
            for k in range(0, i+1):
                if B[2*i-k+1] >= k:
                    for elem in dp[i-k]:
                        dp[i + 1].append(elem  + [s[i-k:i+1]])

        return dp[-1]