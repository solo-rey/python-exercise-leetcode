class Solution:
    # @param board, a 2D array
    # Capture all regions by modifying the input board in-place.
    # Do not return any value.
    def solve(self, board):
        if board is None:
            return
        linenum = len(board)
        colnum = len(board[0])
        visited = [[False for i in range(colnum)] for j in range(linenum)]
        queue = []
        for i in range(colnum):
            if board[0][i] == 'O':
                queue.append((0,i))
            if board[linenum-1][i] == 'O':
                queue.append((linenum-1,i))
        for i in range(1,linenum-1):
            if board[i][0] == 'O':
                queue.append((i,0))
            if board[i][colnum-1] == 'O':
                queue.append((i,colnum-1))
        while len(queue) > 0:
            t = queue.pop()
            if board[t[0]][t[1]] == 'O':
                board[t[0]][t[1]] = '$'
            visited[t[0]][t[1]] = True
            if t[0]+1 < linenum and board[t[0]+1][t[1]] == 'O' and not visited[t[0]+1][t[1]]:
                queue.append((t[0]+1,t[1]))
            if t[0]-1 >= 0 and board[t[0]-1][t[1]] == 'O' and not visited[t[0]-1][t[1]]:
                queue.append((t[0]-1,t[1]))
            if t[1]+1 < colnum and board[t[0]][t[1]+1] == 'O' and not visited[t[0]][t[1]+1]:
                queue.append((t[0],t[1]+1))
            if t[1]-1 >= 0 and board[t[0]][t[1]-1] == 'O' and not visited[t[0]][t[1]-1]:
                queue.append((t[0],t[1]-1))
        for i in range(linenum):
            for j in range(colnum):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                if board[i][j] == '$':
                    board[i][j] = 'O'

