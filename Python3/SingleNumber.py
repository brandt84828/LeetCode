class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        ans = 0
        for v in nums:
            ans = ans ^ v
        
        return ans