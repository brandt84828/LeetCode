#1
class Solution:
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        total = len(nums)*(1+len(nums)) // 2
        miss = total - sum(set(nums)) 
        rep = sum(nums) - sum(set(nums)) 

        ans = []
        ans.append(rep)
        ans.append(miss)
        
        return ans

#2
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        m = {}
        ans = []
        for i in range(1, len(nums)+1):
            if nums[i-1] in m:
                m[nums[i-1]] = m[nums[i-1]] + 1
                if m[nums[i-1]] == 2:
                    ans.append(nums[i-1]) 
            else:
                m[nums[i-1]] = 1
        
        for i in range(1,  len(nums) + 1):
            if i not in m:
                ans.append(i)

        return ans