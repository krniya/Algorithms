def maximalSquare(matrix) -> int:
        m,n = len(matrix), len(matrix[0])
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        maxsq = 0
        for i in range(1, m+1):
            for j in range(1, n+1):
                if matrix[i-1][j-1] == "1":
                    dp[i][j] = min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1]) + 1
                    maxsq = max(maxsq, dp[i][j])
        return maxsq ** 2

def maximalSquare(matrix) -> int:
        m,n = len(matrix), len(matrix[0])
        dp = [0] * (n + 1)
        maxsq, prev = 0, 0
        for i in range(1, m+1):
            for j in range(1, n+1):
                temp = dp[j]
                if matrix[i-1][j-1] == "1":
                    dp[j] = min(dp[j-1], prev, dp[j]) + 1
                    maxsq = max(maxsq, dp[j])
                else:
                    dp[j] = 0
                prev = temp
        return maxsq ** 2

print(maximalSquare([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]))