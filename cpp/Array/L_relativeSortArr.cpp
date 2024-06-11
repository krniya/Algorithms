#include <bits/stdc++.h>
using namespace std;

vector<int> relativeSortArray(vector<int> &a, vector<int> &b)
{
    vector<int> tot(1001);
    for (auto i : a)
        tot[i]++;
    vector<int> ans;
    for (auto i : b)
    {
        if (tot[i])
        {
            while (tot[i]-- > 0)
                ans.emplace_back(i);
        }
    }
    for (int i = 0; i < 1001; i++)
    {
        if (tot[i])
        {
            while (tot[i]-- > 0)
                ans.emplace_back(i);
        }
    }
    return ans;
}