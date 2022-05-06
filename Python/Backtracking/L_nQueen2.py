def totalNQueens(n: int) -> int:
        col,nd,pd = set(),set(),set()
        res = [0]
        board=[["."] * n for _ in range(n)]
        def backtrack(r):
            if r == n:
                global res
                res[0]+=1
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
        return res[0]

print(totalNQueens(4))