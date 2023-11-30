#include <bits/stdc++.h>
using namespace std;

int minimumOneBitOperations(int n)
{
    int res;
    for (res = 0; n > 0; n &= n - 1)
        res = -(res + (n ^ (n - 1)));
    return abs(res);
}