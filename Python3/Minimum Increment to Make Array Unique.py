#1
class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        res = need = 0
        for i in sorted(nums):
            res += max(need - i, 0)
            need = max(need + 1, i + 1)
        return res
# Just Sort, O(NlogN)

#2
class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        c = collections.Counter(nums)
        res = need = 0
        for x in sorted(c):
            res += c[x] * max(need - x, 0) + c[x] * (c[x] - 1) / 2
            need = max(need, x) + c[x]
        return int(res)
# O(KlogK)

#3
class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        root = {}
        def find(x):
            root[x] = find(root[x] + 1) if x in root else x
            return root[x]
        return sum(find(a) - a for a in nums)
# Union Find, O(N)