class Solution:
    def isPalindrome(self, x: int) -> bool:

        y = x
        tmp = 0

        if (x < 0):
            return False

        while(y > 0):
            tmp = tmp * 10 + y % 10
            y = y // 10

        if (x == tmp):
            return True
        
        return False