class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxValue = 0
        count = 0

        for n in nums:
            if n == 1:
                count = count + 1
                maxValue = max(maxValue, count)
            else:
                count = 0
        
        return maxValue