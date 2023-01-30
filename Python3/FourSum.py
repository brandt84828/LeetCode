class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        if len(nums)<4:
            return []
            
        nums.sort()
        res = []

        for i in range(len(nums)-3):
            for j in range(i+1, len(nums)-2):
                k = j + 1
                l = len(nums) - 1
                find = target - nums[i] - nums[j]
                while k < l:
                    if nums[k] + nums[l] < find:
                        k = k + 1
                    elif nums[k] + nums[l] > find:
                        l = l - 1
                    else:
                        if [nums[i], nums[j], nums[k], nums[l]] not in res:
                            res.append([nums[i], nums[j], nums[k], nums[l]])
                        k = k + 1
                        while k < l and nums[k] == nums[k-1]:
                            k = k + 1
        
        return res