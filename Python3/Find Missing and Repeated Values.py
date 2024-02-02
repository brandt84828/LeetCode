#map
class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        record = {}
        res = [0] * 2
        for i in grid:
            for j in i:
                if j in record:
                    record[j] = record[j] + 1
                else:
                    record[j] = 1
        length = len(grid) * len(grid)
        for i in range(1, length+1):
            if i in record:
                if record[i] == 2:
                    res[0] = i
            else:
                res[1] = i
        return res

#math
class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        
        nrow = len(grid)
        ncol = len(grid[0])
        
        _sum = 0
        sum_of_squares = 0
        
        for r in range(nrow):
            for c in range(ncol):
                num = grid[r][c]
                _sum += num
                sum_of_squares += (num ** 2)
        
        n = nrow * ncol
        
        sum_of_1_thru_n = n * (n + 1) // 2
        sum_of_squares_of_1_thru_n = (n * (n + 1) * (2 * n + 1)) // 6
        
        c1 = _sum - sum_of_1_thru_n
        c2 = sum_of_squares - sum_of_squares_of_1_thru_n
        
        duplicate = ((c2 // c1) + c1) // 2 
        missing   = ((c2 // c1) - c1) // 2
        
        return [duplicate, missing]
