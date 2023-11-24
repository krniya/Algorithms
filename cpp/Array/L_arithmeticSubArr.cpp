#include <bits/stdc++.h>
using namespace std;

bool check(vector<int> &arr)
{
    sort(arr.begin(), arr.end()); // Sort the array
    int diff = arr[1] - arr[0];   // Calculate the difference between the first two elements

    // Check if the difference remains the same for consecutive elements
    for (int i = 2; i < arr.size(); i++)
    {
        if (arr[i] - arr[i - 1] != diff)
        {
            return false; // If the difference changes, it's not an arithmetic sequence
        }
    }

    return true; // If all differences are the same, it's an arithmetic sequence
}

// Function to check arithmetic subarrays in the given range
vector<bool> checkArithmeticSubarrays(vector<int> &nums, vector<int> &l, vector<int> &r)
{
    vector<bool> ans; // Vector to store results

    // Iterate through the ranges and check each subarray
    for (int i = 0; i < l.size(); i++)
    {
        // Extract the subarray from nums using the given range [l[i], r[i]]
        vector<int> arr(begin(nums) + l[i], begin(nums) + r[i] + 1);
        ans.push_back(check(arr)); // Check if the subarray forms an arithmetic sequence
    }

    return ans; // Return the results for each subarray
}