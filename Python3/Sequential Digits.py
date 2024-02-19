#1
class Solution:
    def sequentialDigits(self, low, high):
        out = []
        queue = deque(range(1,10))
        while queue:
            elem = queue.popleft()
            if low <= elem <= high:
                out.append(elem)
            last = elem % 10
            if last < 9: queue.append(elem*10 + last + 1)
                    
        return out

#2
class Solution:
    def sequentialDigits(self, low, high):
        ans = []
        for digit in range(1, 9):
            num = next = digit
            while num <= high and next < 10:
                if num >= low:
                    ans.append(num)
                next += 1
                num = num * 10 + next
        return sorted(ans)