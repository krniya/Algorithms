#include<bits/stdc++.h>
using namespace std;


int longestIncreasingPath(vector<vector<int>>& matrix) {
    int m = matrix.size();
    int n = matrix[0].size();
    
    int result = 0;
    
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            result = max(result, dfs(matrix, -1, i, j, m, n));
        }
    }
    
    return result;
}

map<pair<int, int>, int> dp;

int dfs(vector<vector<int>>& matrix, int prev, int i, int j, int m, int n) {
    if (i < 0 || i >= m || j < 0 || j >= n || matrix[i][j] <= prev) {
        return 0;
    }
    if (dp.find({i, j}) != dp.end()) {
        return dp[{i, j}];
    }
    
    int result = 1;
    result = max(result, 1 + dfs(matrix, matrix[i][j], i - 1, j, m, n));
    result = max(result, 1 + dfs(matrix, matrix[i][j], i + 1, j, m, n));
    result = max(result, 1 + dfs(matrix, matrix[i][j], i, j - 1, m, n));
    result = max(result, 1 + dfs(matrix, matrix[i][j], i, j + 1, m, n));
    dp[{i, j}] = result;
    
    return dp[{i, j}];
}