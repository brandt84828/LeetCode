#1
class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        count = {}
        for n in nums:
            if n in count:
                count[n]+=1
            else:
                count[n]=1
        res = 0
        for k, v in count.items():
            if v == 1:
                res += k
        
        return res
        

#2
class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        D, s = defaultdict(int), 0
        for n in nums:
            if D[n] == 0:
                s += n
            elif D[n] == 1:
                s -= n
            D[n] += 1
        return s