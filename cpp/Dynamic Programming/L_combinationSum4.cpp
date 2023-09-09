#include <bits/stdc++.h>
using namespace std;

vector<vector<int>> combinationSum2(vector<int> &candidates, int target)
{
    sort(candidates.begin(), candidates.end());
    vector<vector<int>> result;
    vector<int> combination;
    dfs(candidates, target, result, combination, 0);
    return result;
}

void dfs(vector<int> &nums, int target, vector<vector<int>> &result, vector<int> &combination, int begin)
{
    if (!target)
    {
        result.push_back(combination);
        return;
    }
    for (int i = begin; i < nums.size() && target >= nums[i]; i++)
    {
        combination.push_back(nums[i]);
        // combinationSum1 : dfs(nums, target - nums[i], result, combination, i);
        dfs(nums, target - nums[i], result, combination, i + 1);
        combination.pop_back();
        // combinationSum1 : no this line to filter the duplicate cases
        while (i < nums.size() && nums[i] == nums[i + 1])
            i++;
    }
}

static const int MAX_TARGET = 1010; // Maximum possible target value
int dp[MAX_TARGET];                 // Array to store computed results

int countCombinations(vector<int> nums, int remainingTarget)
{
    // If the remaining target is 0, there's one valid combination.
    if (remainingTarget == 0)
        return 1;

    // If the remaining target becomes negative, it's not possible to reach it.
    if (remainingTarget < 0)
        return 0;

    // If the result for 'remainingTarget' is already computed, return it.
    if (~dp[remainingTarget])
        return dp[remainingTarget];

    int currentCombinations = 0;

    // Iterate through the numbers in 'nums'.
    for (int i = 0; i < nums.size(); i++)
    {
        int currentNum = nums[i];
        // recursively calculate combinations for the new target.
        currentCombinations += countCombinations(nums, remainingTarget - currentNum);
    }

    // Store and return the computed result.
    return dp[remainingTarget] = currentCombinations;
}

int combinationSum4(vector<int> &nums, int target)
{
    // Initialize the 'dp' array with -1 to indicate uncomputed results.
    for (int i = 0; i < MAX_TARGET; i++)
    {
        dp[i] = -1;
    }

    // Start the combination count calculation.
    return countCombinations(nums, target);
}

int main()
{
}