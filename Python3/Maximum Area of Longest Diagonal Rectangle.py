#1 answer
class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        # Get the number of rectangles
        n = len(dimensions)

        # Initialize variables to keep track of maximum area and diagonal
        maxArea = 0
        maxDiag = 0

        # Iterate through each rectangle
        for i in range(n):
            # Get the length and width of the current rectangle
            l, w = dimensions[i]

            # Calculate the square of the diagonal length
            currDiag = l**2 + w**2

            # Compare the current diagonal with the maximum diagonal encountered so far
            # If the current diagonal is greater, or if it's equal but the area is greater,
            # update maxDiag and maxArea accordingly
            if currDiag > maxDiag or (currDiag == maxDiag and l * w > maxArea):
                maxDiag = currDiag
                maxArea = l * w

        # Return the maximum area of the rectangle with the longest diagonal
        return maxArea

#2 Use max key and lambda
class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        a,b = max(dimensions, key = lambda x: (x[0]*x[0]+x[1]*x[1], (x[0]*x[1])))
        return a*b