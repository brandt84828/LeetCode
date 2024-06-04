#1
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        longest = prev = curr = 0

        for bit in nums:
            if bit:
                curr += 1
                longest = max(longest, prev + curr)
            else:
                prev, curr = curr, 0

        return longest - (longest == len(nums))

#2
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        res = 0
        k = 1
        l = 0
        
        for r in range(len(nums)):
            if nums[r] == 0:
                k -= 1

            while k < 0 and l <= r:
                if nums[l] == 0:
                    k += 1
                l += 1
            res = max(res, r-l)
            
        return res