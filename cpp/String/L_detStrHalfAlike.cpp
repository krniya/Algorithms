#include <bits/stdc++.h>
using namespace std;

bool halvesAreAlike(string S)
{
    string vowels = "aeiouAEIOU";
    int mid = S.size() / 2, ans = 0;
    for (int i = 0, j = mid; i < mid; i++, j++)
    {
        if (~vowels.find(S[i]))
            ans++;
        if (~vowels.find(S[j]))
            ans--;
    }
    return ans == 0;
}

bool halvesAreAlike(string s)
{
    set<char> vow = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'};
    int n = s.size() / 2, f = 0;
    for (int i = 0; i < n; i++)
    {
        f += (vow.count(s[i]) - vow.count(s[n + i]));
    }
    return f == 0;
}