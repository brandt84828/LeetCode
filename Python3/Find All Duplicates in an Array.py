class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        result = []

        for i in range(len(nums)):
            n = abs(nums[i])

            if nums[n - 1] < 0:
                result.append(n)
            else:
                nums[n - 1] *= -1

        return result

#Initialize an empty vector ans to store the duplicates.
#Iterate through the array nums.
#For each element nums[i], take its absolute value x.
#Check if nums[x-1] is negative.
#If it is, then x is a duplicate, so add it to ans.
#Otherwise, mark nums[x-1] as negative.
#eturn ans.