#1
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort(reverse=True)
        i, j = 0, len(people) - 1
        while i <= j:
            if people[i] + people[j] <= limit: j -= 1
            i += 1
        return i

#2
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        left = 0
        right = len(people) - 1
        boat = 0
        while left<=right:
            if people[left]+people[right]<=limit:
                boat += 1
                right -= 1
                left += 1
            else:
                boat += 1
                right -= 1

        return boat