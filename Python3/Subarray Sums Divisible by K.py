class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        result, running_sum = 0,0
        mod_array = [1] + [0]*  k
        for i in range(len(nums)):
            running_sum += nums[i]
            result += mod_array[running_sum % k]
            mod_array[running_sum % k]+=1
        return result