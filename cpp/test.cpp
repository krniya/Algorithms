#include <bits/stdc++.h>
using namespace std;

bool containsDuplicate(vector<int> nums)
{
    unordered_set<int> visited;
    for (int num : nums)
    {
        if (visited.find(num) != visited.end())
            return true;
        visited.insert(num);
    }
    return false;
}

int main()
{
    vector<int> nums{1, 2, 3, 4, 5, 6, 7};
    bool res = containsDuplicate(nums);
    cout << res;
}