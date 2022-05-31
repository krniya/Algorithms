def solveNQueens(n):
        col,nd,pd = set(),set(),set()
        res = []
        board=[["."] * n for _ in range(n)]
        def backtrack(r):
            if r == n:
                c = ["".join(row) for row in board]
                res.append(c)
                return
            for c in range(n):
                if c in col or (r+c) in pd or (r-c) in nd:
                    continue
                col.add(c)
                pd.add(r+c)
                nd.add(r-c)
                board[r][c] = "Q"
                backtrack(r+1)
                col.remove(c)
                pd.remove(r+c)
                nd.remove(r-c)
                board[r][c] = "."
        backtrack(0)
        return res

print(solveNQueens(4))