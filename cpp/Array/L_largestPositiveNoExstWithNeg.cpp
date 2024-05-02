#include <bits/stdc++.h>
using namespace std;

int findMaxK(std::vector<int> &nums)
{
    std::sort(nums.begin(), nums.end());
    int left = 0, right = nums.size() - 1;
    int maxK = std::numeric_limits<int>::min();
    while (left < right)
    {
        int sum = nums[left] + nums[right];
        if (sum == 0)
        {
            maxK = std::max(maxK, nums[right]);
            left++;
            right--;
        }
        else if (sum < 0)
        {
            left++;
        }
        else
        {
            right--;
        }
    }
    return maxK != std::numeric_limits<int>::min() ? maxK : -1; // If no such pair found
}