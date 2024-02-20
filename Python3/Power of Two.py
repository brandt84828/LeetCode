#1
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        count = 0

        while n > 0:
            count = count + (n & 1)
            n = n >> 1

        return count == 1

#2
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        s = bin(n)
        s = str(s)

        s = s.replace("0" , "")[1:];
        print(s)
        if(len(s) == 1):
            return True
        else:
            return False

#3
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
       return n > 0 and not(n & (n - 1))