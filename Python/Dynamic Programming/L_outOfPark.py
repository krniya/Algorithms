def findPaths(m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        cache = {}
        def dfs(i,j,mm):
            if (i,j,mm) in cache:
                return cache[(i,j,mm)]
            if mm < 0:
                return 0
            if i<0 or j<0 or i==m or j==n:
                return 1
            a = dfs(i+1,j,mm-1)
            b = dfs(i-1,j,mm-1)
            c = dfs(i,j+1,mm-1)
            d = dfs(i,j-1,mm-1)
            cache[(i,j,mm)] = a + b + c + d
            return (a + b + c + d) 
        return dfs(startRow, startColumn, maxMove) % 1000000007