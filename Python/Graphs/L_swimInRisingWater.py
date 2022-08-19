import heapq


def swimInWater(grid) -> int:
        n =len(grid)
        visited = set()
        minH = [[grid[0][0], 0, 0]]
        visited.add((0,0))
        direction = [(1,0),(-1,0),(0,1),(0,-1)]
        while minH:
            t, r, c = heapq.heappop(minH)
            if r==n-1 and c==n-1:
                return t
            for dr, dc in direction:
                neiR, neiC = r + dr, c + dc
                if neiR < 0 or neiC < 0 or neiR == n or neiC == n or (neiR, neiC) in visited:
                    continue
                visited.add((neiR, neiC))
                heapq.heappush(minH, [max(t, grid[neiR][neiC]), neiR, neiC])