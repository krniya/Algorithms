#include<bits/stdc++.h>
using namespace std;

vector<vector<int>> combinationSum2(vector<int>& candidates, int target) {
        sort(candidates.begin(), candidates.end());
        vector<vector<int>> result;
        vector<int> combination;
        dfs(candidates, target, result, combination, 0);
        return result;
    }
    
    void dfs(vector<int>& nums, int target, vector<vector<int>>& result, vector<int>& combination, int begin) {
        if (!target) {
            result.push_back(combination);
            return;
        }
        for (int i = begin; i < nums.size() && target >= nums[i]; i++) {
            combination.push_back(nums[i]);
            //combinationSum1 : dfs(nums, target - nums[i], result, combination, i);
            dfs(nums, target - nums[i], result, combination, i + 1);
            combination.pop_back();
            //combinationSum1 : no this line to filter the duplicate cases 
            while (i < nums.size() && nums[i] == nums[i+1]) i++;
        }
    }

int main() {

}