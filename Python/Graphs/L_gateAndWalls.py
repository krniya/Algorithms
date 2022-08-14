from collections import deque


def wallsAndGate(grid):
    ROW, COL = len(grid), len(grid[0])
    queue = deque()
    distance = 1
    direction = [(0,1), (0,-1),(1,0),(-1,0)]
    for r in range(ROW):
        for c in range(COL):
            if grid[r][c] == 0:
                queue.append((r,c))
    while queue:
        for _ in range(len(queue)):
            r,c = queue.popleft()
            for dr, dc in direction:
                row, col = r + dr, c + dc
                if row <0 or row == ROW or col < 0 or col == COL or grid[row][col] != float("inf"):
                    continue
                grid[row][col] = distance
                queue.append((row, col))
        distance += 1
    return grid


print(wallsAndGate([[float("inf"),-1,0,float("inf")],
                   [float("inf"),float("inf"),float("inf"),-1],
                   [float("inf"),-1,float("inf"),-1],
                   [0,-1,float("inf"),float("inf")]]))