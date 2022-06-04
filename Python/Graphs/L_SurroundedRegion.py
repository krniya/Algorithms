def solve(board) -> None:
        row, col = len(board), len(board[0])
        def dfs(r,c):
            if r < 0 or c < 0 or r == row or c == col or board[r][c] != "O":
                return
            board[r][c] = "C"
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)
            
        for r in range(row):
            for c in range(col):
                if board[r][c] == "O" and (r in [0, row-1] or c in [0, col-1]):
                    dfs(r,c)
        
        for r in range(row):
            for c in range(col):
                if board[r][c] == "O":
                    board[r][c] = "X" 
                
        for r in range(row):
            for c in range(col):
                if board[r][c] == "C":
                    board[r][c] = "O" 