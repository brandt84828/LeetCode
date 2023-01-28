class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        diff = float('inf')
        res = 0
        
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            j, k = i + 1, len(nums) - 1
            while j < k:
                sum = nums[i] + nums[j] + nums[k]
                if abs(target - sum) < diff:
                    diff = abs(target - sum)
                    res = sum
                if sum == target:
                    return res
                elif sum < target:
                    j = j + 1
                else:
                    k = k - 1
        
        return res