#include <bits/stdc++.h>
using namespace std;

bool PredictTheWinner(vector<int> &nums)
{
    vector<int> dp(nums);

    for (int len = 2; len <= nums.size(); len++)
    {
        for (int i = 0; i + len - 1 < nums.size(); i++)
        {
            dp[i] = max(nums[i] - dp[i + 1], nums[i + len - 1] - dp[i]);
        }
    }

    return dp[0] >= 0;
}