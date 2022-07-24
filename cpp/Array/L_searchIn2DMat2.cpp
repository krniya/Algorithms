#include<bits/stdc++.h>
using namespace std;

bool searchMatrix(vector<vector<int>>& matrix, int target) {
    int i = 0, j = matrix[0].size() - 1;
    while (i < matrix.size() && j > -1) {
        if (target > matrix[i][j]) i++;
        else if (target < matrix[i][j]) j--;
        else return true;
    } 
    return false;
}

int main() {

}