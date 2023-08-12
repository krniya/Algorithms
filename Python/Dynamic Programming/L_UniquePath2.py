from typing import List


def uniquePathsWithObstacles(og) -> int:
        if og[-1][-1] or og[0][0]:
            return 0
        m,n=len(og),len(og[0])
        og[0][0] = 1
        for i in range(1,m):
            og[i][0] = int(og[i][0] == 0 and og[i-1][0] == 1)
        for j in range(1, n):
            og[0][j] = int(og[0][j] == 0 and og[0][j-1] == 1)

        for i in range(1,m):
            for j in range(1,n):
                if og[i][j] == 0:
                    og[i][j] = og[i-1][j] + og[i][j-1]
                else:
                    og[i][j] = 0
        return og[m-1][n-1]
    
    


def uniquePathsWithObstacles1(obstacle_grid: List[List[int]]) -> int:
        ROW, COL = len(obstacle_grid), len(obstacle_grid[0])
        cache = {}
        def find_path(row, col):
            if (row, col) in cache:
                return cache[(row, col)]
            if row == ROW or col == COL:
                return 0
            if obstacle_grid[row][col] == 1:
                return 0
            if row == ROW - 1 and col == COL - 1:
                return 1
            cache[(row, col)] = find_path(row + 1, col) + find_path(row, col + 1)
            return cache[(row, col)]
        return find_path(0,0)