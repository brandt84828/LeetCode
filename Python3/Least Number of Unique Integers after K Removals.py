#1
class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        c = Counter(arr)
        s = sorted(arr,key = lambda x:(c[x],x))
        return len(set(s[k:]))

#2
class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        count = Counter(arr)
        ans = len(count)
        for i in sorted(count.values()):
            k -= i
            if k < 0:
                break
            ans -= 1
        return ans
