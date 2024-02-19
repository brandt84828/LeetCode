class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        res = 0
        for index, v in enumerate(nums):
            if len(nums) % (index + 1) == 0:
                res += v * v
        
        return res