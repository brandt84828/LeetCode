class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        insert = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                nums[insert] = nums[i]
                insert = insert + 1
        return insert