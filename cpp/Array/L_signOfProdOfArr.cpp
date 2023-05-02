#include <bits/stdc++.h>
using namespace std;

int arraySign(vector<int> &nums)
{
    int signFunc = 1;
    for (int number : nums)
    {
        if (number == 0)
            return 0;
        if (number < 0)
            signFunc *= -1;
    }
    return signFunc;
}