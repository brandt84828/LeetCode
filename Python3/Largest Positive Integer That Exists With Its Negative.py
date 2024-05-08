#1
class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        # [1] two use two-pointers approach, we need
        #     to prepare the list by sorting
        nums.sort()
        
        # [2] move pointers towards each other to find
        #     largest positive integer with its negative
        i, j = 0, len(nums)-1
        while i < j:
            if nums[i] == - nums[j]:
                return nums[j]
            if abs(nums[i]) > abs(nums[j]):
                i += 1
            else:
                j -= 1
                
        return -1

#2
class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        nums = set(nums)
        numMap = defaultdict(int)
        for num in nums :
            numMap[abs(num)] += 1
        
        res = -1
        for num in numMap :
            if numMap[num] == 2 :
                res = max(res,num)
        return res
#3
class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        s, ans = set(), -1
        for n in nums:
            if -n in s:
                ans = max(ans, abs(n))
            s.add(n)
        return ans