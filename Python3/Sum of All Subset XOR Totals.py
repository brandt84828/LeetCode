#1
class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        # Time complexity: O(n), Space: O(1)
        bits = 0
        for a in nums:
            bits |= a
        return bits * int(pow(2, len(nums)-1))

        # M × 2 ^ (K - 1)

#2
class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        sumTotal = 0

        for num in nums:
            sumTotal |= num
        return sumTotal << (len(nums) - 1)