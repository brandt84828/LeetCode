class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        size = len(grid) - 2
        res = []
        for i in range(1, size + 1):
            temp = []
            for j in range(1 , size + 1):
                # get max V
                maxV = 0
                for row in range(i - 1, i + 2):
                    for col in range(j - 1, j + 2):
                        maxV = max(maxV, grid[row][col])
                temp.append(maxV)
            res.append(temp)

        return res