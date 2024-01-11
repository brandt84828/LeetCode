class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        cur_sum , min_sum = 0, 0

        for num in nums:
            cur_sum = cur_sum + num
            min_sum = min(min_sum, cur_sum)
        
        if min_sum > 0:
            return 1
        else:
            return 1 - min_sum
        