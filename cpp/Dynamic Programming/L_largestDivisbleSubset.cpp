#include <bits/stdc++.h>
using namespace std;

vector<int> largestDivisibleSubset(vector<int> &nums)
{
    sort(nums.begin(), nums.end());
    int n = nums.size();
    vector<int> groupSize(n, 1), prevElement(n, -1);
    int maxIndex = 0;

    for (int i = 0; i < n; ++i)
    {
        for (int j = 0; j < i; ++j)
        {
            if (nums[i] % nums[j] == 0 && groupSize[i] < groupSize[j] + 1)
            {
                groupSize[i] = groupSize[j] + 1;
                prevElement[i] = j;
            }
        }
        if (groupSize[i] > groupSize[maxIndex])
        {
            maxIndex = i;
        }
    }

    vector<int> result;
    for (int i = maxIndex; i != -1; i = prevElement[i])
    {
        result.insert(result.begin(), nums[i]);
    }
    return result;
}

int n;
vector<int> ans;
void solve(vector<int> &nums, int i, int j, vector<int> cur)
{
    if (j >= n)
    {
        if (cur.size() > ans.size())
            ans = cur;
        return;
    }
    for (int k = j; k < n; k++)
    {
        if (nums[k] % nums[i] == 0)
        {
            cur.push_back(nums[k]);
            solve(nums, k, k + 1, cur);
            cur.pop_back();
        }
    }
    if (cur.size() > ans.size())
        ans = cur;
}
vector<int> largestDivisibleSubset(vector<int> &nums)
{
    n = nums.size();
    int mx = 0;
    sort(nums.begin(), nums.end());
    vector<int> cur;
    for (int i = 0; i < n; i++)
    {
        solve(nums, i, i + 1, {nums[i]});
    }
    return ans;
}