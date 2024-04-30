#1
class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        n = len(mat)
        m = len(mat[0])
        #taking transpose of matrix 
        lst = [[mat[j][i] for j in range(n)] for i in range(m)] 
        res = 0
        for i in range(n):
            for j in range(m):
                #Checking if current element is 1 and sum of elements of current row and column is also 1
                if mat[i][j] == 1 and sum(mat[i]) == 1 and sum(lst[j]) == 1:
                    res += 1
        return res

#2
class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        r = list(map(lambda x:sum(x)==1, mat))
        c = list(map(lambda x:sum(x)==1, zip(*mat)))
        print(*mat)
        return sum(r[i] and c[j] and v for i, row in enumerate(mat) for j, v in enumerate(row))