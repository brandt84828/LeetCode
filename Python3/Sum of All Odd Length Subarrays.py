#1 Brute-Force
class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        n = len(arr)
        res = 0
        for l in range(1, n + 1, 2):
            for i in range(n - l + 1):
                res += sum(arr[i:i + l])
        return res

#2 Math
class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        res, n = 0, len(arr)
        for i, a in enumerate(arr):
            res += ((i + 1) * (n - i) + 1) // 2 * a
        return res