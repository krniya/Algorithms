#include <bits/stdc++.h>
using namespace std;

double myPow(double x, int n)
{
    if (n < 0)
        return 1.0 / pow(x, (long long)-1 * n);
    return pow(x, (long long)n);
}

double pow(double x, long long n)
{
    if (n == 0)
        return 1;
    if (n % 2 == 0)
        return pow(x * x, n / 2);
    else
        return x * pow(x * x, (n - 1) / 2);
}