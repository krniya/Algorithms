#include<bits/stdc++.h>
using namespace std;

int diagonalSum(vector<vector<int>>& mat) {
        int n = mat.size();
        int totsum = 0;
        int i=0,jl = 0, jr = n-1;
        while(i<n) {
            totsum += mat[i][jl];
            totsum += mat[i][jr];
            i++;
            jl++;
            jr--;
        }
        if(n%2) totsum -= mat[n/2][n/2];
        return totsum;
    }