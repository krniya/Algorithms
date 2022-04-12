class Solution:
    def gameOfLife(self, board):
        m,n = len(board), len(board[0])
        def neighbour(i,j):
            count = 0
            for i,j in [(i-1,j-1),(i-1,j),(i-1,j+1),(i,j-1),(i,j+1),(i+1,j-1),(i+1,j),(i+1,j+1)]:
                if 0 <= i < m and 0<= j < n and board[i][j] == 1:
                    count += 1
            return count
        
        zero = []
        one = []
        for i in range(m):
            for j in range(n):
                neiCount = neighbour(i,j)
                if neiCount < 2 or neiCount > 3:
                    zero.append((i,j))
                elif neiCount == 3:
                    one.append((i,j))
        for i,j in zero:
            board[i][j] = 0
        for i,j in one:
            board[i][j] = 1