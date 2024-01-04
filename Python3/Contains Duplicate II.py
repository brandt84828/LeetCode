class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        ans = {}
        for i in range(len(nums)):
            if nums[i] in ans:
                diff = abs(i - ans[nums[i]])
                if diff <= k:
                    return True
                else:
                    ans[nums[i]] = i
            else:
                ans[nums[i]] = i
        
        return False