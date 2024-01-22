#include <bits/stdc++.h>
using namespace std;

vector<int> findErrorNums(vector<int> &nums)
{
    int n = nums.size();
    unordered_map<int, int> mp;
    for (int i = 1; i <= n; i++)
        mp[i]++;

    for (auto a : nums)
        mp[a]--;
    int duplicate = 0, missing = 0;

    for (auto a : mp)
    {
        if (a.second == -1)
            duplicate = a.first;
        if (a.second == 1)
            missing = a.first;
    }

    return {duplicate, missing};
}

vector<int> findErrorNums1(vector<int> &nums)
{
    int n = nums.size();
    int actual_sum = n * (n + 1) / 2;
    int array_sum = 0;
    int unique_sum = 0;
    unordered_set<int> s(nums.begin(), nums.end());

    for (int a : nums)
    {
        array_sum += a;
    }

    for (int a : s)
    {
        unique_sum += a;
    }

    int missing = actual_sum - unique_sum;
    int duplicate = array_sum - unique_sum;

    return {duplicate, missing};
}