

#include <bits/stdc++.h>
using namespace std;

int largestAltitude(vector<int> &gains)
{
    int largestAlt = 0, currentAlt = 0;
    for (int gain : gains)
    {
        currentAlt += gain;
        if (currentAlt > largestAlt)
            largestAlt = currentAlt;
    }
    return largestAlt;
}
