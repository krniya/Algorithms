#include <bits/stdc++.h>
using namespace std;

int maxFrequency(vector<int> &nums, int k)
{
    sort(nums.begin(), nums.end());
    int left = 0, right = 0;
    long res = 0, total = 0;

    while (right < nums.size())
    {
        total += nums[right];

        while (nums[right] * static_cast<long>(right - left + 1) > total + k)
        {
            total -= nums[left];
            left += 1;
        }

        res = max(res, static_cast<long>(right - left + 1));
        right += 1;
    }

    return static_cast<int>(res);
}