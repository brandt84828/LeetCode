class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        inventory = {}
        count = 0
        for s in stones:
            if s in inventory:
                inventory[s] = inventory[s] + 1
            else:
                inventory[s] = 1
        
        for s in jewels:
            count = count + inventory.get(s, 0)
        
        return count

#2
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        count = 0

        for s in stones:
            if s in jewels:
                count +=1
        
        return count

#3
class Solution:
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
            
        return sum([i in J for i in S])

#4
class Solution:
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        count = 0
        for i in range(0,len(J)):
            count = count + S.count(J[i])
            
        return count