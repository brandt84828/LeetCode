class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        total = 0
        zero_count = 0

        for num in nums:
            if num == 0:
                zero_count = zero_count + 1
                total = total + zero_count
            else:
                zero_count = 0
        
        return total