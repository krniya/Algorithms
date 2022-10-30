from collections import deque


def shortestPath(grid, k: int) -> int:
        rows, cols = len(grid), len(grid[0])
        q = deque()
        # r, c, pathLength, remaining_k
        q.append((0, 0, 0, k))
        seen = set()

        while q:
            r, c, pathLength, kRemain = q.popleft()
            if (r, c, kRemain) in seen or kRemain < 0:
                continue

            if r == (rows - 1) and c == (cols - 1):
                return pathLength

            seen.add((r, c, kRemain))
            if grid[r][c] == 1:
                kRemain -= 1
                
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if nr in range(rows) and nc in range(cols):
                    q.append((nr, nc, pathLength + 1, kRemain))

        return -1