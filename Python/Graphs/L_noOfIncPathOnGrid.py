from functools import lru_cache


def countPaths(grid) -> int:
        rows = len(grid)
        cols = len(grid[0])
        mod = 10 ** 9 + 7

        @lru_cache(None)
        def count(row, col):
            res = 1
            for dx, dy in [[row, col + 1], [row, col - 1], [row + 1, col], [row - 1, col]]:
                if 0 <= dx < rows and 0 <= dy < cols and grid[dx][dy] > grid[row][col]:
                    res += count(dx, dy) % mod
            return res

        count_values = []
        for i in range(rows):
            for j in range(cols):
                count_values.append(count(i, j))
        path_sum = sum(count_values) % mod

        return path_sum