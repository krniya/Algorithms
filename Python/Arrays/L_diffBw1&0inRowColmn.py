from typing import List


def onesMinusZeros(grid: List[List[int]]) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])
        res = [[0] * n for _ in range(m)]
        ones_row = [row.count(1) for row in grid]
        ones_col = [col.count(1) for col in zip(*grid)]

        for i in range(m):
            for j in range(n):
                res[i][j] = ones_row[i] + ones_col[j] - (m - ones_row[i]) - (n - ones_col[j])

        return res