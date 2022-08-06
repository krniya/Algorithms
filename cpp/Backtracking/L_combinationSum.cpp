#include<bits/stdc++.h>
using namespace std;

vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        vector<vector<int>> res;
        sort(candidates.begin(), candidates.end());
        vector<int> curr;
        backtrack(candidates, target, 0, 0, curr, res);
        return res;
    }
    void backtrack(vector<int>& candidates, int target, int sum, int start, vector<int>& curr, vector<vector<int>>& result) {
        if (sum > target) {
            return;
        }
        if (sum == target) {
            result.push_back(curr);
            return;
        }
        for (int i = start; i < candidates.size(); i++) {
            curr.push_back(candidates[i]);
            backtrack(candidates, target, sum + candidates[i], i, curr, result);
            curr.pop_back();
        }
    }

int main() {

}