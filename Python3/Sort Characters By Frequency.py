#1
class Solution:
    def frequencySort(self, s: str) -> str:
        # Count the occurence on each character
        cnt = {}
        for c in s:
            if c in cnt:
                cnt[c] += 1
            else:
                cnt[c] = 1
        
        # Sort and Build string
        res = []
        for k, v in sorted(cnt.items(), key = lambda x: -x[1]):
            res += [k] * v
        return "".join(res)

#2
class Solution:
    def frequencySort(self, s: str) -> str:
        # Count the occurence on each character
        cnt = collections.Counter(s)
        
        # Build string
        res = []
        for k, v in cnt.most_common():
            res += [k] * v
        return "".join(res)

#3
class Solution:
    def frequencySort(self, s: str) -> str:
        # Count the occurence on each character
        cnt = collections.Counter(s)
        
        # Build heap
        heap = [(-v, k) for k, v in cnt.items()]
        heapq.heapify(heap)
        
        # Build string
        res = []
        while heap:
            v, k = heapq.heappop(heap)
            res += [k] * -v
        return ''.join(res)