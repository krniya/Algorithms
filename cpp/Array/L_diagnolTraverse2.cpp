#include <bits/stdc++.h>
using namespace std;

vector<int> findDiagonalOrder(vector<vector<int>> &nums)
{
    vector<int> res;
    queue<pair<int, int>> q;
    q.push({0, 0});

    while (!q.empty())
    {
        auto p = q.front();
        q.pop();
        res.push_back(nums[p.first][p.second]);

        if (p.second == 0 && p.first + 1 < nums.size())
        {
            q.push({p.first + 1, 0});
        }

        if (p.second + 1 < nums[p.first].size())
        {
            q.push({p.first, p.second + 1});
        }
    }

    return res;
}