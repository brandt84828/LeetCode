class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        maxAvg = -10000
        total = 0
        start = 0

        for i in range(len(nums)):
            total = total + nums[i]
            if i + 1 - start == k:
                maxAvg = max(maxAvg, total / k)
                total = total - nums[start]
                start = start + 1
        
        return maxAvg

#2 better
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        
        # Initialize currSum and maxSum to the sum of the initial k elements
        currSum = maxSum = sum(nums[:k])

        # Start the loop from the kth element 
        # Iterate until you reach the end
        for i in range(k, len(nums)):

            # Subtract the left element of the window
            # Add the right element of the window
            currSum += nums[i] - nums[i - k]
            
            # Update the max
            maxSum = max(maxSum, currSum)

        # Since the problem requires average, we return the average
        return maxSum / k