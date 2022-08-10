#include<bits/stdc++.h>
using namespace std;


bool exist(vector<vector<char>>& board, string word) {
    int r = board.size(), c = board[0].size();
    for(int i=0;i<r;i++) {
        for(int j=0;j<c;j++) {
            if(board[i][j] == word[0] and dfs(i,j,r,c,0,board,word)) return true;
        }
    }
    return false;
}
bool dfs(int i, int j, int r, int c, int idx, vector<vector<char>>& board, string word) {
    if(i < 0 or i >= r or j < 0 or j >= c or word[idx] != board[i][j]) return false;
    if(idx == word.size() - 1) return true;
    board[i][j] = '-';
    if(dfs(i+1,j,r,c,idx+1,board,word) or
        dfs(i-1,j,r,c,idx+1,board,word) or
        dfs(i,j+1,r,c,idx+1,board,word) or
        dfs(i,j-1,r,c,idx+1,board,word)) return true;
    board[i][j] = word[idx];
    return false;
}

int main() {

}