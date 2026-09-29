class Solution:
    def recursion(self,board,word,c,i,j):
        if len(word)==c:
            return True
        
        if 0<=i<len(board) and 0<=j<len(board[0]):
            if board[i][j]==word[c]:
                board[i][j]='#'
                ans=self.recursion(board,word,c+1,i+1,j) or self.recursion(board,word,c+1,i-1,j) or self.recursion(board,word,c+1,i,j+1) or self.recursion(board,word,c+1,i,j-1)
                board[i][j]=word[c]
                return ans
        return False

    def exist(self, board: List[List[str]], word: str) -> bool:
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.recursion(board,word,0,i,j):
                    return True
        return False
        