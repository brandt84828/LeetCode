#1
class Solution:
    def numberOfMatches(self, n: int) -> int:
        return n - 1

#2
class Solution:
    def numberOfMatches(self, n: int) -> int:
        m = 0
        while n>1:
            if n%2 == 0:
                n = n/2
                m+=n
            else:
                n = ((n-1)/2)+1
                m+= (n-1)
        return int(m)