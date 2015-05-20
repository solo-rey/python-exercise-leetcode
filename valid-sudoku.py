class Solution:
    # @param board, a 9x9 2D array
    # @return a boolean
    def isValidSudoku(self, board):
        if not board or len(board) != 9 or len(board[0]) != 9:
            return False
        for i in range(9):
            dic = [False for k in range(9)]
            for j in range(9):
                if board[i][j] != '.':
                    if dic[ord(board[i][j]) - ord('1')]:
                        return False
                    dic[ord(board[i][j]) - ord('1')] = True
        for j in range(9):
            dic = [False for k in range(9)]
            for i in range(9):
                if board[i][j] != '.':
                    if dic[ord(board[i][j]) - ord('1')]:
                        return False
                    dic[ord(board[i][j]) - ord('1')] = True

        for block in range(9):
            dic = [False for k in range(9)]
            for i in range(block/3*3,block/3*3+3):
                for j in range(block%3*3,block%3*3+3):
                    if board[i][j] != '.':
                        if dic[ord(board[i][j]) - ord('1')]:
                            return False
                        dic[ord(board[i][j]) - ord('1')] = True
        return True

