#include <bits/stdc++.h>
using namespace std;

vector<string> buildArray(vector<int> &target, int n)
{
    unordered_set<int> target_set(target.begin(), target.end());
    vector<std::string> result;

    for (int i = 1; i <= target.back(); ++i)
    {
        if (target_set.find(i) != target_set.end())
        {
            result.push_back("Push");
        }
        else
        {
            result.push_back("Push");
            result.push_back("Pop");
        }
    }
    return result;
}