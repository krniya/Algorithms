#include <bits/stdc++.h>
using namespace std;

string maximumOddBinaryNumber(string s)
{
    sort(s.rbegin(), s.rend());
    for (int i = s.size() - 1; i >= 0; i--)
    {
        if (s[i] == '1')
            swap(s[i], s[s.size() - 1]);
    }
    return s;
}