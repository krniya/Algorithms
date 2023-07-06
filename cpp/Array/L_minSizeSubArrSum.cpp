#include <bits/stdc++.h>
using namespace std;

int minSubArrayLen(int target, vector<int> &A)
{
    int i = 0;
    int j = 0;
    int sum = 0;
    int ans = 1000000;
    while (j < A.size())
    {
        sum += A[j];
        while (sum >= target)
        {
            ans = std::min(ans, j - i + 1);
            sum -= A[i];
            i++;
        }
        j++;
    }
    return (ans == 1000000) ? 0 : ans;
}