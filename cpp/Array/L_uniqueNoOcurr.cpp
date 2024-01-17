#include <bits/stdc++.h>
using namespace std;

bool uniqueOccurrences(vector<int> &arr)
{
    unordered_map<int, int> hashMap;
    for (int i = 0; i < arr.size(); i++)
    {
        if (hashMap.find(arr[i]) != hashMap.end())
        {
            hashMap[arr[i]]++;
        }
        else
        {
            hashMap[arr[i]] = 1;
        }
    }
    unordered_set<int> hashSet;
    for (auto &pair : hashMap)
    {
        if (!hashSet.insert(pair.second).second)
        {
            return false;
        }
    }
    return true;
}