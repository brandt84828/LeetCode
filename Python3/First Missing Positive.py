#1
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.append(0)
        n = len(nums)
        for i in range(len(nums)): #delete those useless elements
            if nums[i]<0 or nums[i]>=n:
                nums[i]=0
        print(nums)
        for i in range(len(nums)): #use the index as the hash to record the frequency of each number
            nums[nums[i]%n]+=n
        print(nums)
        for i in range(1,len(nums)):
            print(nums[i]/n)
            if nums[i] < n:
                return i
        return n

#So consider an array like [1,4,3,3,3]. The length is 5, so n = 5. For each item, we are basically overwriting the spot at the index of the item with 5 + spot. So, at index 0 we have a 1, and 1%5 is 1, so we replace the item at index 1 with 5 + that item. Now our array is [1,9,3,3,3]. Next, at index 1 we have a 9, and 9%5 is 4 (notice how adding 5 didn't change the fact that we can still find the original value with % 5), so we replace the item at index 4 with 5 + that item. Our array is now [1, 9, 3, 3, 8]. Continuing, we get [1, 9, 3, 8, 8] then [1, 9, 3, 13, 8] and finally [1, 9, 3, 18, 8]. When we iterate through to find the values at the end, starting at index 1, we find that 9/5 is greater than 1, 3/5 is not greater than 1, 13/5 and 8/5 are greater than 1. Thus, since 3/5 is the first not greater than 5, we know index 2 was never used or added to, so 2 is the missing number. Feel free to comment if you have Qs or if I made any mistakes.

#2
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        for i,num in enumerate(nums):
            if num <= 0:
                nums[i] = 0

        for i,num in enumerate(nums):
            index = abs(num)-1
            if index >= 0 and index < len(nums):
                if nums[index] == 0:
                    nums[index] = -inf
                elif nums[index] > 0: # we dont want to make negative to be positive again, when its duplicated num
                    nums[index] *= -1
        print(nums)
        for index,num in enumerate(nums):
            if num >= 0:
                return index + 1

        return len(nums) + 1