class Solution:
    def reverseBits(self, n: int) -> int:
        ans = 0
        for i in range(32):
            ans = ans << 1
            if (n & 1) != 0:
                ans = ans + 1
            #ans = ans + (n & 1)
            n = n >> 1
        return ans

#way2
class Solution:
    def reverseBits(self, n: int) -> int:
        n = '{:032b}'.format(n) # convert into to binary string
        n = n[::-1]             # reverse string
        n = int(n, 2)           # convert string into integer base 2
        return n