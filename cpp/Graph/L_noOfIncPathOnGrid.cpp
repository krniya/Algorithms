#include <bits/stdc++.h>
using namespace std;

int countPaths(vector<vector<int>> &grid)
{
    int rows = grid.size();
    int cols = grid[0].size();
    int mod = 1e9 + 7;

    vector<vector<int>> dp(rows, vector<int>(cols, -1));

    for (int i = 0; i < rows; i++)
    {
        for (int j = 0; j < cols; j++)
        {
            if (dp[i][j] == -1)
            {
                helper(i, j, grid, dp, -1);
            }
        }
    }

    long long pathSum = 0;
    for (int i = 0; i < rows; i++)
    {
        for (int j = 0; j < cols; j++)
        {
            pathSum = (pathSum + dp[i][j]) % mod;
        }
    }
    return static_cast<int>(pathSum);
}

int helper(int row, int col, vector<vector<int>> &grid, vector<vector<int>> &dp, int parent)
{
    int rows = grid.size();
    int cols = grid[0].size();
    int mod = 1e9 + 7;

    if (row < 0 || row >= rows || col < 0 || col >= cols || grid[row][col] <= parent)
    {
        return 0;
    }

    if (dp[row][col] != -1)
    {
        return dp[row][col];
    }

    int down = helper(row + 1, col, grid, dp, grid[row][col]) % mod;
    int up = helper(row - 1, col, grid, dp, grid[row][col]) % mod;
    int right = helper(row, col + 1, grid, dp, grid[row][col]) % mod;
    int left = helper(row, col - 1, grid, dp, grid[row][col]) % mod;

    return dp[row][col] = (down + up + right + left + 1) % mod;
}