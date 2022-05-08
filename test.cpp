int add(char ch){
    if(ch == '(') return 1;
    else return -1;
}

class Solution {
public:
    bool hasValidPath(vector<vector<char>>& grid) {
        
        int n = grid.size(), m = grid[0].size();
        if(grid[0][0] == ')') return false;
        int mtk[n+1][m+1][n+m+2];
        for(int i=0;i<=n;i++) for(int j=0;j<=m;j++) for(int k=0;k<=n+m+1;k++) mtk[i][j][k] = false;
        mtk[0][0][add(grid[0][0])] = true;
        for(int i=0;i<n;i++){
            for(int j=0;j<m;j++){
                for(int k=0;k<i+j+2;k++){
                    if(mtk[i][j][k] == false) continue;
                    if(i+1 < n){
                                 int ni = k + add(grid[i+1][j]);
                          if(ni>=0) mtk[i+1][j][ni] |= mtk[i][j][k];
                    }
                    if(j+1<m){
                    int nj = k + add(grid[i][j+1]);
                    if(nj>=0) mtk[i][j+1][nj] |= mtk[i][j][k];
                        
                    }
           
                  
                }
            }
        }
        return mtk[n-1][m-1][0];
    }
};