class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        start = 0
        end = len(nums) - 1
        ans = [0] * len(nums)

        for i in range(len(nums)-1,-1,-1):
            if abs(nums[start]) > abs(nums[end]):
                ans[i] = nums[start] * nums[start]
                start = start + 1
            else:
                ans[i] = nums[end] * nums[end]
                end = end - 1
        return ans