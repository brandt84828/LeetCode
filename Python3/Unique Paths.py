#1
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        row = [1] * n
        for i in range(m-1):
            newRow = [1] * n
            for j in range(n - 2, -1, -1):
                newRow[j] = newRow[j+1] + row[j]
            row = newRow
        
        return row[0]

#2
class Solution:
    def uniquePaths(self, m, n):
        @cache
        def dfs(i, j):
            if i >= m or j >= n:      return 0
            if i == m-1 and j == n-1: return 1
            return dfs(i+1, j) + dfs(i, j+1)
        return dfs(0, 0)

#3
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0] * n] * m

        for i in range(m):
            dp[i][0] = 1
        for i in range(n):
            dp[0][i] = 1
        
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        
        return dp[m-1][n-1]
