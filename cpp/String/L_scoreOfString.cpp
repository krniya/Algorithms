#include <bits/stdc++.h>
using namespace std;

int scoreOfString(string s)
{
    int ans = 0;
    for (int i = 1; i < s.size(); i++)
    {
        ans += abs(s[i - 1] - s[i]);
    }
    return ans;
}