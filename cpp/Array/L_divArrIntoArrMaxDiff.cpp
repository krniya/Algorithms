#include <bits/stdc++.h>
using namespace std;

vector<vector<int>> divideArray(vector<int> &nums, int k)
{
    int size = nums.size();

    sort(nums.begin(), nums.end());

    vector<vector<int>> result(size / 3, vector<int>(3));
    int groupIndex = 0;
    for (int i = 0; i < size; i += 3)
    {
        if (i + 2 < size && nums[i + 2] - nums[i] <= k)
        {
            result[groupIndex] = {nums[i], nums[i + 1], nums[i + 2]};
            groupIndex++;
        }
        else
        {
            return vector<vector<int>>();
        }
    }
    return result;
}

vector<vector<int>> divideArray(vector<int> &nums, int k)
{
    vector<vector<int>> res;
    sort(nums.begin(), nums.end());
    for (int i = 2; i < nums.size(); i += 3)
    {
        if (nums[i] - nums[i - 2] > k)
            return {};
        res.push_back({nums[i - 2], nums[i - 1], nums[i]});
    }
    return res;
}