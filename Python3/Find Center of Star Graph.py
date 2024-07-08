#1
class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        m = {}
        for edge in edges:
            for point in edge:
                if point not in m:
                    m[point] = 1
                else:
                    m[point] += 1
        
        for k, v in m.items():
            if v == len(edges):
                return k
        
        
#2
class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        x,y = edges[0][0], edges[0][1]
        if x==edges[1][0] or x == edges[1][1]:
            return x
        return y
        
        
#3
class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        return edges[0][edges[0][1] in edges[1]]        
        
#4
class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        return (set(edges[0]) & set(edges[1])).pop()    
        