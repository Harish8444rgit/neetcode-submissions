class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        col=[1]*len(matrix)
        row=[1]*len(matrix[0])
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]==0:
                    col[i]=0
                    row[j]=0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if col[i]==0 or row[j] ==0:
                    matrix[i][j]=0
        
        