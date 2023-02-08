class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        res[0] = 1
        for i in range(1, len(nums)):
            res[i] = nums[i-1] * res[i-1]
        temp = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] = res[i] * temp
            temp = temp * nums[i]

        return res
        