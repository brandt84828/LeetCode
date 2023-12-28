#1
class Solution:
    def numberOfSteps(self, num: int) -> int:
        count = 0
        while (num!=0):
            if (num % 2 == 0):
                num = num // 2
                count = count + 1
            else:
                num = num -  1
                count = count + 1
        return count

#2
class Solution:
    def numberOfSteps(self, num: int) -> int:
        count = -(num>0)
        while (num!=0):
            count = count + 1 + (num & 1)
            num = num >> 1
        return count