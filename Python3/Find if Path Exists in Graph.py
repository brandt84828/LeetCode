#1 DFS
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        neighbors = defaultdict(list)
        for n1, n2 in edges:
            neighbors[n1].append(n2)
            neighbors[n2].append(n1)
        print(neighbors)
            
        def dfs(node, destination, seen):
            if node == destination:
                return True
            if node in seen:
                return False
            
            seen.add(node)
            for n in neighbors[node]:
                if dfs(n, destination, seen):
                    return True
                
            return False
        
        seen = set()    
        return dfs(source, destination, seen)

#2 BFS
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        neighbors = defaultdict(list)
        for n1, n2 in edges:
            neighbors[n1].append(n2)
            neighbors[n2].append(n1)
            
        q = deque([source])
        seen = set([source])
        while q:
            node = q.popleft()            
            if node == destination:
                return True            
            for n in neighbors[node]:
                if n not in seen:
                    seen.add(n)
                    q.append(n)
                
        return False