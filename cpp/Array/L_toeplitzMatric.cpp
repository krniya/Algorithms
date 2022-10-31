#include<bits/stdc++.h>
using namespace std;

bool isToeplitzMatrix(vector<vector<int>>& m) {
    for (int i = 1; i < m.size(); i++)
        for (int j = 0; j < m[0].size()-1; j++)
            if (m[i-1][j] != m[i][j+1]) return false;
    return true;
}