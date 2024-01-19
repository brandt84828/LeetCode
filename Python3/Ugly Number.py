#1
class Solution:
    def isUgly(self, n: int) -> bool:
        for p in 2, 3, 5:
            while n % p == 0 < n:
                n /= p
        return n == 1

#2
class Solution:
    def isUgly(self, n: int) -> bool:
        while n >= 1:
            if n%2 == 0:
                n=n//2
            elif n%3 == 0:
                n=n//3
            elif n%5 == 0:
                n=n//5
            elif n == 1:
                return True
            else:
                return False