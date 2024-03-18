#1
class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        s = set(p[0] for p in paths)                  
        for path in paths:
            if path[1] not in s:                         
                return path[1]

#2
class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        A, B = map(set, zip(*paths))
        return (B - A).pop()