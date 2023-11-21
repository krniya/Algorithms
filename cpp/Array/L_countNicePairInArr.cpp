#include <bits/stdc++.h>
using namespace std;

int countNicePairs(vector<int> &nums)
{
    int res = 0;
    const int mod = 1e9 + 7;
    unordered_map<int, int> count;

    for (int n : nums)
    {
        int r = rev(n);
        int cur = count[n - r];
        count[n - r] = cur + 1;
        res = (res + cur) % mod;
    }

    return res;
}

int rev(int num)
{
    int reversedNum = 0;

    while (num > 0)
    {
        int digit = num % 10;
        reversedNum = reversedNum * 10 + digit;
        num = num / 10;
    }

    return reversedNum;
}