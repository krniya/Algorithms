#include <bits/stdc++.h>
using namespace std;

vector<int> getRow(int r)
{
    vector<int> v(r + 1);
    long temp = 1;
    v[0] = v[r] = 1;
    for (int i = 1, up = r, down = 1; i < r; i++, up--, down++)
    {
        temp = temp * up / down;
        v[i] = temp;
    }
    return v;
}