#include <bits/stdc++.h>
using namespace std;

int rangeBitwiseAnd(int left, int right)
{
    int cnt = 0;
    while (left != right)
    {
        left >>= 1;
        right >>= 1;
        cnt++;
    }
    return (left << cnt);
}