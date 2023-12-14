class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        maxWealth = 0

        for i in range(0, len(accounts)):
            temp = 0
            for j in range(0, len(accounts[i])):
                temp = temp + accounts[i][j]
            if temp > maxWealth:
                maxWealth = temp
        
        return maxWealth