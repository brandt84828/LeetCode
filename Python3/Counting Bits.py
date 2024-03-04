#1
class Solution:
    def countBits(self, n: int) -> List[int]:
        counter = [0]
        for i in range(1, n+1):
            counter.append(counter[i >> 1] + i % 2)
        return counter

#2
class Solution:
    def countBits(self, n: int) -> List[int]:
        return [bin(i).count('1') for i in range(n+1)]

#3
class Solution:
    def countBits(self, n: int) -> List[int]:
        nextOrder = 2
        tracker = 0
        counter = [0]*(n+1)

        for i in range(1, n+1):
            if i == nextOrder:
                nextOrder *= 2
                tracker = 0
            counter[i] = counter[tracker] + 1
            tracker += 1
        return counter

#4
class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0] * (n + 1)
        offset = 1
        for i in range(1, n + 1):
            if offset * 2 == i:
                offset *= 2
            ans[i] = ans[i - offset] + 1
        return ans