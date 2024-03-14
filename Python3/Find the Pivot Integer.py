#1 Math : use (n+1)*n/2
class Solution:
    def pivotInteger(self, n: int) -> int:
        pivot = 0
        total = (1 + n) * n // 2
        for i in range(1, n + 1):
            pivot = (1 + i) * i // 2
            if total - pivot + i == pivot:
                return i
        
        return -1

#2 Math : use sqrt & (n+1)*n/2
class Solution:
    def pivotInteger(self, n: int) -> int:
        x = sqrt(n * (n + 1) / 2)

        if x % 1 != 0:
            return -1
        else:
            return int(x)