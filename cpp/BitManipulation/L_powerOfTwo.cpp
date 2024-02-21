#include <bits/stdc++.h>
using namespace std;

bool isPowerOfTwo(int n)
{
    return n > 0 && not(n & n - 1);
}