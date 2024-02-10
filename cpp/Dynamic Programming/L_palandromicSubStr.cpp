#include <bits/stdc++.h>
using namespace std;

int countSubstrings(string s)
{
    int res = 0;
    for (int i = 0; i < s.size(); i++)
    {
        res += countPal(s, i, i);
        res += countPal(s, i, i + 1);
    }
    return res;
}
int countPal(string s, int l, int r)
{
    int res = 0;
    while (l >= 0 and r < s.size() and s[l] == s[r])
    {
        res++;
        l--;
        r++;
    }
    return res;
}

int countSubstrings(string s)
{
    int n = s.length(), ans = 0;
    for (int i = 0; i < n; ++i)
    {
        int even = palindromeCount(s, i, i + 1);
        int odd = palindromeCount(s, i, i);
        ans += even + odd;
    }
    return ans;
}

int palindromeCount(const string &s, int left, int right)
{
    int count = 0;
    while (left >= 0 && right < s.length() && s[left] == s[right])
    {
        --left;
        ++right;
        ++count;
    }
    return count;
}