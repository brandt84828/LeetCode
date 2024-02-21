#1
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxCandies = max(candies)
        result = []
        for i in range(len(candies)):
            if candies[i]+extraCandies >= maxCandies:
                result.append(True)
            else:
                result.append(False)
        return result
        

#2
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxCandies = max(candies)
        return [candy+extraCandies >= maxCandies for candy in candies]
        