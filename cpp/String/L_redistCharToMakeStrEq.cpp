#include <bits/stdc++.h>
using namespace std;

bool makeEqual(vector<string> &words)
{
    unordered_map<char, int> map;
    for (auto it : words)
    {
        for (auto i : it)
        {
            map[i]++;
        }
    }
    int n = words.size();
    for (auto it : map)
    {
        if (it.second % n == 0)
            continue;
        else
            return false;
    }
    return true;
}