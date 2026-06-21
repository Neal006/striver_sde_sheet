from ast import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        r = [False]*len(matrix)
        c = [False]*len(matrix[0])
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    r[i] = True
                    c[j] = True
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if r[i] or c[j]:
                    matrix[i][j] = 0