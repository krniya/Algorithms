#include <bits/stdc++.h>
using namespace std;

int bulbSwitch(int n)
{
    int i = 0;
    while (1)
    {
        if (i * i > n)
            return i - 1;
        i++;
    }
}