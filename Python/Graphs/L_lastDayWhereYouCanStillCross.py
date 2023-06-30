import collections

def latestDayToCross(row: int, col: int, cells) -> int:
        def isPossible(mid):
            grid = [[0] * col for _ in range(row)]
            for i, j in cells[:mid]:
                grid[i-1][j-1] = 1
            queue = collections.deque()
            for i in range(col):
                if not grid[0][i]:
                    queue.append((0,i))
                    grid[0][i] = -1
                    
            while queue:
                r, c = queue.popleft()
                if r == row-1:
                    return True
                for dr, dc in [(0,1), (0,-1), (1,0),(-1,0)]:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < row and 0 <= nc < col and grid[nr][nc] == 0:
                        queue.append((nr,nc))
                        grid[nr][nc] = -1
            return False
        
        left, right = 1, len(cells)
        while left < right:
            mid = right - (right - left) // 2
            if isPossible(mid):
                left = mid
            else:
                right = mid - 1
        return left