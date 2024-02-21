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

int rangeBitwiseAnd1(int left, int right)
{
    while (right > left)
    {
        // The below statement is used to calculate the total number of bits in right and the NUMBER is updated accordingly.``
        // Since we do not need to calculate till it reaches value 0, and right needs to be greater than left, while loop check condition is put that way
        right = right & (right - 1);
    }
    return right;
}