class Solution:
    def findMin(self, nums: List[int]) -> int:
        start , end = 0 ,len(nums) - 1 
        minValue = float("inf")
        
        while start  <  end :
            mid = (start + end ) // 2
            minValue = min(minValue, nums[mid])
            
            # right has the min 
            if nums[mid] > nums[end]:
                start = mid + 1
                
            # left has the  min 
            else:
                end = mid - 1 
                
        return min(minValue,nums[start])
