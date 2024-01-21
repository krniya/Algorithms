#include <bits/stdc++.h>
using namespace std;

int rob(vector<int> &nums)
{
    int prev = 0;
    int curr = 0;
    int next = 0;

    for (int i = 0; i < nums.size(); i++)
    {
        next = max(prev + nums[i], curr);
        prev = curr;
        curr = next;
    }

    return curr;
}

int rob1(vector<int> &nums)
{
    int n = nums.size();
    vector<int> dp(n, -1);
    if (n == 0)
        return 0;
    if (n == 1)
        return nums[0];

    int ans = helper(n - 1, nums, dp);
    return ans;
}

int helper(int ind, vector<int> nums, vector<int> &dp)
{
    if (ind == 0)
        return nums[ind];
    if (ind == -1)
        return 0;
    if (dp[ind] != -1)
        return dp[ind];
    int pick = nums[ind] + helper(ind - 2, nums, dp);
    int non_pick = 0 + helper(ind - 1, nums, dp);
    return dp[ind] = max(pick, non_pick);
}