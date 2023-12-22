class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        rt = len(nums)
        for i in range(len(nums)):
            rt = rt ^ i ^ nums[i]

        return rt


#2

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # use math
        total = int((1 + len(nums)) / 2 * len(nums))

        sum = 0

        for n in nums:
            sum += n

        return total - sum

#3

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = len(nums)

        for i in range(len(nums)):
            res += i - nums[i]
        return res
