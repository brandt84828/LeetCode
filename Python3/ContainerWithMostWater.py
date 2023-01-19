class Solution:
    def maxArea(self, height: List[int]) -> int:

        l = 0
        r = len(height) - 1
        maxArea = 0

        while l < r:

            width = r - l
            maxArea = max(maxArea, min(height[l], height[r]) * width)

            if height[l] <= height[r]:
                l = l + 1
            else:
                r = r - 1
        
        return maxArea