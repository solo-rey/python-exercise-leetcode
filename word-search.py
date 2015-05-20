class Solution:
    # @param board, a list of lists of 1 length string
    # @param word, a string
    # @return a boolean
    def exist(self, board, word):
        visited = [[False for i in range(len(board[0]))] for j in range(len(board))]
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.helper(board,word,0,i,j,visited):
                    return True
        return False

    def helper(self,board,word,index,row,col,visited):
        if index == len(word):
            return True
        if row < 0 or col < 0 or row >= len(board) or col >= len(board[0]):
            return False
        if visited[row][col]:
            return False
        if board[row][col] != word[index]:
            return False
        visited[row][col] = True
        res = self.helper(board,word,index+1,row-1,col,visited) or \
                self.helper(board,word,index+1,row,col+1,visited) or \
                self.helper(board,word,index+1,row+1,col,visited) or\
                self.helper(board,word,index+1,row,col-1,visited)
        visited[row][col] = False
        return res