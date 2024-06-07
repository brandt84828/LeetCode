#1
class Solution:
    def numSteps(self, s: str) -> int:
        n, count = 0, 0
        for i in range(len(s)):
            n = n + int(math.pow(2, i)) * int(s[len(s) - i - 1])
        
        while n != 1:
            if n % 2 != 0:
                n = n + 1
            else:
                n = n // 2
            count += 1
        
        return count

#2
class Solution:
    def numSteps(self, s: str) -> int:
        ans = 0
        carry = 0
        n = len(s)
        for i in range(n-1, 0, -1):  # Except first digit
            if int(s[i]) + carry == 1:  # Odd number
                carry = 1
                ans += 2  # 2 operations: Add 1 and divide by two
            else:
                ans += 1  # 1 operation: Divide by 2
        return ans + carry