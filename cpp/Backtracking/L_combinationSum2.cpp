#include<bits/stdc++.h>
using namespace std;

vector<vector<int>> combinationSum2(vector<int>& candidates, int target) {
    sort(candidates.begin(), candidates.end());
    vector<vector<int>> res;
    vector<int> curr;
    backtrack(0,candidates,target, res,curr);
    return res;
}
void backtrack(int i, vector<int>& candidates, int tar, vector<vector<int>>& res, vector<int>& curr) {
    if (!tar) {
        res.push_back(curr);
        return;
    }
    for(int j=i; j<candidates.size();j++) {
        if (j>i and candidates[j] == candidates[j-1]) continue;
        if (candidates[j] > tar) break;
        curr.push_back(candidates[j]);
        backtrack(j+1, candidates, tar - candidates[j], res, curr);
        curr.pop_back();
    }
}

int main() {

}