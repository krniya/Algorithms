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