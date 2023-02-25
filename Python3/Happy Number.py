class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()
        while n != 1:
            total = 0
            while n > 0:
                digit = n % 10
                total = total + digit * digit
                n = n // 10
            if total in visited:
                return False
            visited.add(total)
            n = total
        return True
#最快解法 縮一起

def ishappy(n):
    a = []
    while n not in a:
        a.append(n)
        n = sum([int(x) ** 2 for x in str(n)])

    return 'happy' if n == 1 else 'unhappy'