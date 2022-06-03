class NumMatrix {
public:
    vector<vector<int>> sum;
    NumMatrix(vector<vector<int>>& matrix) {
        int m = matrix.size();
        int n = matrix[0].size();
        sum = vector<vector<int>>(m+1, vector<int>(n+1));
        for (int r=1; r<m+1; ++r) {
            for (int c=1; c<n+1; ++c) {
                sum[r][c] = sum[r][c-1] + sum[r-1][c] - sum[r-1][c-1] + matrix[r-1][c-1];
            }
        }
    }
    
    int sumRegion(int row1, int col1, int row2, int col2) {
        row1++;
        col1++;
        row2++;
        col2++;
        return sum[row2][col2] - sum[row1-1][col2] - sum[row2][col1-1] + sum[row1-1][col1-1];
    }
};