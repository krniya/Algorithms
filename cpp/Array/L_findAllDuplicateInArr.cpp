#include <bits/stdc++.h>
using namespace std;

vector<int> findDuplicates(vector<int> &nums)
{
    vector<int> result;
    for (int i = 0; i < nums.size(); i++)
    {
        int num = abs(nums[i]);
        if (nums[num - 1] < 0)
            result.push_back(num);
        nums[num - 1] = nums[num - 1] * -1;
    }
    return result;
}