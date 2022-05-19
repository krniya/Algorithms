
def longestIncreasingPath(matrix) -> int:
        m, n = len(matrix), len(matrix[0])
        dp = [[-1] * n for _ in range(m)]
        
        def dfs(i, j, prev):
            if i < 0 or j < 0 or i >= m or j >= n or matrix[i][j] <= prev:
                return 0

            if dp[i][j] != -1:
                return dp[i][j]

            left = dfs(i, j - 1, matrix[i][j])
            right = dfs(i, j + 1, matrix[i][j])
            top = dfs(i - 1, j, matrix[i][j])
            bottom = dfs(i + 1, j, matrix[i][j])
            
            dp[i][j] = max(left, right, top, bottom) + 1
            return dp[i][j]
        
        ans = -1
        for i in range(m):
            for j in range(n):
                ans = max(ans, dfs(i, j, -1))
        return ans