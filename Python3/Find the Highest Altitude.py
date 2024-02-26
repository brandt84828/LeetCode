#1
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        res = 0
        total = 0
        for n in gain:
            total = total + n
            if total > res:
                res = total
        
        return res
        
#2
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        curr_alt=0
        max_alt=0
        for i in range(0,len(gain)):
            curr_alt+=gain[i]
            max_alt=max(max_alt,curr_alt)
        return max_alt

#3 accumulate > Iter
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
       return max(0, max(accumulate(gain)))
			