#1
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        m = {}
        ans = {}
        for i in arr:
            if i in m:
                m[i] = m[i] + 1
            else:
                m[i] = 0
        
        for k, v in m.items():
            if v in ans:
                return False
            else:
                ans[v] = 0
        
        return True

#2
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        count = {}

        for n in arr:
            if n in count: 
                count[n] += 1
            else: 
                count[n] = 1
        
        return len(count.values()) == len(set(count.values()))

#3
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        c = collections.Counter(arr)
        return len(c) == len(set(c.values())) 