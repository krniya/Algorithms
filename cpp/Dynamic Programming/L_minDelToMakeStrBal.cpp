#include <bits/stdc++.h>
using namespace std;

int minimumDeletions(string s)
{
    int aCount = 0;
    int bCount = 0;
    int output = INT_MAX;
    for (int i = 0; i < s.length(); i++)
        aCount += ('b' - s[i]);

    for (int i = 0; i < s.length(); i++)
    {
        output = fmin(output, aCount + bCount);
        aCount -= ('b' - s[i]);
        bCount += (s[i] - 'a');
    }

    output = fmin(output, aCount + bCount);
    return output;
}
