class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        newSet = set()

        for value in nums:
            if value in newSet:
                return True
            else:
                newSet.add(value)
        return False
