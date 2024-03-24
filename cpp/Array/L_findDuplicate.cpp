#include <bits/stdc++.h>
using namespace std;
int findDuplicate(vector<int> &nums)
{
    int slow = 0, fast = 0;
    do
    {
        slow = nums[slow];
        fast = nums[nums[fast]];
    } while (slow != fast);
    int slow1 = 0;
    do
    {
        slow = nums[slow];
        slow1 = nums[slow1];
    } while (slow != slow1);
    return slow;
}

int findDuplicate(std::vector<int> &nums)
{
    int left = 1;
    int right = nums.size() - 1;

    while (left < right)
    {
        int mid = left + (right - left) / 2;
        int count = 0;

        // Count the numbers less than or equal to mid
        for (int num : nums)
        {
            if (num <= mid)
            {
                count++;
            }
        }

        // If count is greater than mid, the duplicate lies in the left half
        if (count > mid)
        {
            right = mid;
        }
        else
        { // Otherwise, it lies in the right half
            left = mid + 1;
        }
    }

    return left;
}
int main()
{
}