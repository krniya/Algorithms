from collections import deque


def orangesRotting(grid) -> int:
        queue = deque()
        fresh, time = 0,0
        direction = [(0,1), (0,-1), (1,0), (-1,0)]
        ROW, COL = len(grid), len(grid[0])
        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    queue.append((r,c))
        while queue and fresh:
            for i in range(len(queue)):
                r, c = queue.popleft()
                for dr, dc in direction:
                    row, col = r+dr, c+dc
                    if row < 0 or row == ROW or col < 0 or col == COL or grid[row][col]!= 1:
                        continue
                    grid[row][col] = 2
                    fresh -= 1
                    queue.append((row, col))
            time += 1
        return -1 if fresh else time

print(orangesRotting([[2,1,1],[1,1,0],[0,1,1]]))