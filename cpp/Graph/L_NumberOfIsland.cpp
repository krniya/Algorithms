#include<bits/stdc++.h>
using namespace std;


int numIslands(vector<vector<char>>& grid) {
    int m = grid.size(), n = grid[0].size();
    int count = 0;
    for(int i=0;i<m;i++) {
        for(int j=0;j<n;j++) {
            if(grid[i][j] == '1') {
                dfs(i,j,grid,m,n);
                count++;
            }
        }
    }
    return count;
}
void dfs(int i, int j, vector<vector<char>>& grid, int m, int n) {
    if(i<0 or i>=m or j<0 or j>=n or grid[i][j] != '1') return;
    grid[i][j] = '#';
    dfs(i+1,j,grid,m,n);
    dfs(i-1,j,grid,m,n);
    dfs(i,j+1,grid,m,n);
    dfs(i,j-1,grid,m,n);
}

int main() {

}