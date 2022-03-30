def calculateMinimumHP(dungeon):
    ROW, COL = len(dungeon), len(dungeon[0])
    res = [[float("inf")] * (COL + 1) for r in range(ROW + 1)]
    res[ROW][COL - 1] = res[ROW - 1][COL] = 1
    for r in range(ROW - 1, -1, -1):
        for c in range(COL - 1, -1, -1):
            res[r][c] = max(min(res[r][c+1],res[r+1][c]) - dungeon[r][c], 1)
    return res[0][0]