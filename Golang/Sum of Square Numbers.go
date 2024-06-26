#1
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        for a in range(int(sqrt(c))+1):
            b = sqrt(c - a*a)
            if b == int(b):
                return True
        return False

# Time: O(sqrt(c) * logC), Space: O(1)

#2
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        squareSet = set()
        for x in range(int(math.sqrt(c)) + 1):
            squareSet.add(x * x)

        for aSquare in squareSet:
            bSquare = c - aSquare
            if bSquare in squareSet:
                return True
        return False

# Time: O(sqrt(c)), Space: O(sqrt(c))

#3
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        left = 0
        right = int(sqrt(c))
        while left <= right:
            cur = left * left + right * right
            if cur == c: return True
            if cur < c:
                left += 1
            else:
                right -= 1
        return False

# Time: O(sqrt(c)), Space: O(1)