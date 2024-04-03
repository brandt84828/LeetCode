#1
class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        res = []
        for column in range(len(matrix[0])):
            temp = []
            for row in range(len(matrix)):
                temp.append(matrix[row][column])
            res.append(temp)

        return res

#2
class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        rows, cols = len(matrix), len(matrix[0])
        result = [[0 for _ in range(rows)] for _ in range(cols)]
        for i in range(rows):
            for j in range(cols):
                result[j][i] = matrix[i][j]
        return result