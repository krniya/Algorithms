#include <bits/stdc++.h>
using namespace std;

int constrainedSubsetSum(vector<int> &nums, int k)
{
    int n = nums.size();
    priority_queue<pair<int, int>> pq; // max heap to maintain the elements of dp vector in descending order
    pq.push({nums[0], 0});             // as we can not have empty subsequence
    vector<int> dp(n, 0);              // dp vector for storing maximum sum that can be achieved till ith element
    dp[0] = nums[0];
    int ans = nums[0];
    for (int i = 1; i < n; i++)
    {
        while (!pq.empty()) // find maximum element from dp vector in the range [i-k, i-1]
        {
            auto p = pq.top();
            if (i - p.second > k)
                pq.pop();
            else
                break;
        }
        // check if the current element must be first element of subsequence or not
        dp[i] = max(nums[i], nums[i] + pq.top().first);
        ans = max(ans, dp[i]);
        pq.push({dp[i], i});
    }
    return ans;
}