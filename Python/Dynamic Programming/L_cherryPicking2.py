from typing import List


def cherryPickup(grid: List[List[int]]) -> int:
    ROW, COL = len(grid), len(grid[0])
    cache = {}
    def dfs(r,c1,c2):
        if (r,c1,c2) in cache:
            return cache[(r,c1,c2)]
        if c1==c2 or min(c1,c2) < 0 or max(c1,c2) == COL:
            return 0
        if (r == ROW-1):
            return grid[r][c1] + grid[r][c2]
        res = 0
        for r1 in [-1,0,1]:
            for r2 in [-1,0,1]:
                res = max(res, dfs(r+1,c1+r1,c2+r2))
        cache[(r,c1,c2)] = res + grid[r][c1] + grid[r][c2]
        return cache[(r,c1,c2)]
    return dfs(0,0,COL-1)