#include <bits/stdc++.h>
using namespace std;

vector<int> sortedSquares(vector<int> &nums)
{
    int n = nums.size(), l = 0, r = n - 1;
    vector<int> ans(n);
    for (int i = n - 1; i >= 0; i--)
    {
        int xl = nums[l] * nums[l], xr = nums[r] * nums[r];
        if (xl > xr)
        {
            ans[i] = xl;
            l++;
        }
        else
        {
            ans[i] = xr;
            r--;
        }
    }
    return ans;
}