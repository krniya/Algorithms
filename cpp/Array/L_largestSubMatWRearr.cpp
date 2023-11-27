#include <bits/stdc++.h>
using namespace std;

int largestSubmatrix(vector<vector<int>> &matrix)
{
    int row = matrix.size();
    int col = matrix[0].size();

    // Calculate heights for each column
    for (int i = 1; i < row; i++)
    {
        for (int j = 0; j < col; j++)
        {
            if (matrix[i][j] == 1)
            {
                matrix[i][j] += matrix[i - 1][j];
            }
        }
    }

    int res = 0;
    for (int i = 0; i < row; i++)
    {
        // Sort the heights in ascending order
        sort(matrix[i].begin(), matrix[i].end());

        // Iterate through the sorted heights
        for (int j = 0; j < col; j++)
        {
            int height = matrix[i][j];
            int width = col - j;
            res = max(res, height * width);
        }
    }

    return res;
}