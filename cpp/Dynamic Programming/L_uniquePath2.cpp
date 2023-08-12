#include <bits/stdc++.h>
using namespace std;

int uniquePathsWithObstacles(vector<vector<int>> &obstacleGrid)
{
    int m = obstacleGrid.size(), n = obstacleGrid[0].size();
    vector<vector<int>> dp(m + 1, vector<int>(n + 1, 0));
    dp[0][1] = 1;
    for (int i = 1; i <= m; ++i)
        for (int j = 1; j <= n; ++j)
            if (!obstacleGrid[i - 1][j - 1])
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1];
    return dp[m][n];
}

int m, n;
vector<vector<int>> dp;
int uniquePathsWithObstacles(vector<vector<int>> &obstacleGrid)
{
    m = size(obstacleGrid), n = size(obstacleGrid[0]);
    dp.resize(m, vector<int>(n));
    return solve(obstacleGrid, 0, 0);
}
// function to recursively explore all unique paths and store the results once calculated
int solve(vector<vector<int>> &grid, int i, int j)
{
    if (i < 0 || j < 0 || i >= m || j >= n)
        return 0; // bounds checking
    if (grid[i][j])
        return dp[i][j] = 0; // obstacle found at current cell
    if (i == m - 1 && j == n - 1)
        return 1; // reached bottom-right of grid ? return 1
    if (dp[i][j])
        return dp[i][j];                                             // if already computed for current cell, just return the stored results
    return dp[i][j] = solve(grid, i + 1, j) + solve(grid, i, j + 1); // recursively explore the two options available with us
}