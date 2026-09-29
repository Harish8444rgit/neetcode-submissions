class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # transpose 
        r=len(matrix)
        c=len(matrix[0])
        for i in range(r):
            for j in range(i,c):
                matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
        # reverse each row
        for i in range(r):
            matrix[i]=matrix[i][::-1]

        