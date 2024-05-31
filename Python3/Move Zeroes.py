#1
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)-1,-1,-1):

            if (nums[i] == 0):
                nums.pop(i)
                nums.append(0)

        print(nums)
        

#2
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        index = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[index], nums[i] = nums[i], nums[index]
                index += 1
        return