from functools import cache
from typing import List


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

def minFallingPathSum(matrix: List[List[int]]) -> int:
    n = len(matrix)
    m = len(matrix[0])
    dp = [[0] * m for _ in range(n)]

    for j in range(m):
        dp[0][j] = matrix[0][j]

    for i in range(1, n):
        for j in range(m):
            ld = rd = float('inf')
            up = matrix[i][j] + dp[i - 1][j]

            if j - 1 >= 0:
                ld = matrix[i][j] + dp[i - 1][j - 1]
            if j + 1 < m:
                rd = matrix[i][j] + dp[i - 1][j + 1]

            dp[i][j] = min(up, min(ld, rd))

    mini = dp[n - 1][0]
    for j in range(1, m):
        mini = min(mini, dp[n - 1][j])
    return mini