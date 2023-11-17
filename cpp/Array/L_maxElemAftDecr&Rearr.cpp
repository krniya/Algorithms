#include <bits/stdc++.h>
using namespace std;

int maximumElementAfterDecrementingAndRearranging(vector<int> &arr)
{
    sort(arr.begin(), arr.end());
    int maxVal = 1;

    for (int i = 1; i < arr.size(); i++)
    {
        if (arr[i] > maxVal)
        {
            maxVal += 1;
        }
    }

    return maxVal;
}