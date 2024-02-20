#1
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        r = nums[0]
        imax = r
        imin = r

        for i in range(1, len(nums)):
            if nums[i] < 0:
                imax, imin = imin, imax
            
            imax = max(nums[i], imax * nums[i])
            imin = min(nums[i], imin * nums[i])

            r = max(r, imax)
        return r
        

#2
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        B = nums[::-1]
        for i in range(1, len(nums)):
            nums[i] *= nums[i - 1] or 1
            B[i] *= B[i - 1] or 1
        return max(nums + B)
        