

from collections import defaultdict


def equalPairs(grid) -> int:
        count = 0
        counter = defaultdict(int)
        for row in grid:
            counter[tuple(row)] += 1
        for col in range(len(grid)):
            colm = []
            for row in range(len(grid)):
                colm.append(grid[row][col])
            count += counter[tuple(colm)]
        return count