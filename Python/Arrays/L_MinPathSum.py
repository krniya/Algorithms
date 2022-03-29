def minPathSum(grid):
    m = len(grid)
    n = len(grid[0])
    for i in range(1, n):
        grid[0][i] += grid[0][i-1]
    for i in range(1, m):
        grid[i][0] += grid[i-1][0]
    for i in range(1, m):
        for j in range(1, n):
            grid[i][j] += min(grid[i-1][j], grid[i][j-1])
    return grid[-1][-1]

def minPathSum2(grid):
    ROW, COL = len(grid), len(grid[0])
    res = [[float("inf")] * (COL + 1) for r in range(ROW + 1)]
    res[ROW - 1][COL] = 0
    for r in range(ROW - 1, -1, -1):
        for c in range(COL - 1, -1, -1):
            res[r][c] = grid[r][c] + min(res[r+1][c], res[r][c+1])
    return res[0][0]


print(minPathSum([[1,3,1],[1,5,1],[4,2,1]]))