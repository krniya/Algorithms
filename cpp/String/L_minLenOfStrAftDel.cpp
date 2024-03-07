#include <bits/stdc++.h>
using namespace std;

int minimumLength(string s)
{
    int left = 0, right = s.size() - 1;
    while (left < right and s[left] == s[right])
    {
        int current = s[left];
        while (left <= right and s[left] == current)
            left++;
        while (left <= right and s[right] == current)
            right--;
    }
    return right - left + 1;
}