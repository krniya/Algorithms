#include<bits/stdc++.h>
using namespace std;

bool checkXMatrix(vector<vector<int>>& v1) {
    int n = v1.size();
    for(int i=0; i<n; i++){
        for(int j=0; j<n; j++){
            if(i==j || (i+j) == n-1){
                if(v1[i][j]==0)     return false;
            }
            else if(v1[i][j]!=0)     return false;
        }
    }
    return true;
}

int main() {
    vector<int> num = {12,45,65,43,23,54,76};
    twoS tws;
    vector<int> ans = tws.twoSum(num, 88);
}