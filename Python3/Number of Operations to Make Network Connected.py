class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:

        if len(connections) < n-1:
            return -1
        g = [set() for i in range(n)]
        for i, j in connections:
            g[i].add(j)
            g[j].add(i)
        visited = [0] * n

        def dfs(node):
            if visited[node]:
                return 0
            visited[node] = 1
            for i in g[node]:
                dfs(i)
            return 1
        
        return sum(dfs(i) for i in range(n)) - 1
            