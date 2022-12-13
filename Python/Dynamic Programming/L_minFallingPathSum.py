from functools import cache

def minFallingPathSum(matrix) -> int:
        row, col = len(matrix), len(matrix[0])
        res = float("inf")
        @cache
        def dfs(r,c):
            if c<0 or c==col:
                return float("inf")
            if r == row - 1:
                return matrix[r][c]
            return matrix[r][c] + min(dfs(r+1,c-1), dfs(r+1, c), dfs(r+1,c+1))

        for i in range(col):
            res = min(res, dfs(0, i))
        return res
