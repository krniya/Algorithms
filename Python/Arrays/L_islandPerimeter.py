def islandPerimeter(grid) -> int:
    dir = [(1,0), (0,1), (-1,0), (0,-1)]
    result = 0
    m,n = len(grid), len(grid[0])
    for i in range(m):
        for j in range(n):
            if grid[i][j]:
                result += 4
                for dr, dc in dir:
                    if 0<=i+dr<m and 0<=j+dc<n and grid[i+dr][j+dc]:
                        result-=1
    return result

print(islandPerimeter([[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]))