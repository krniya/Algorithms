#include <bits/stdc++.h>
using namespace std;

int minOperations(string s)
{
    int op_count_even = 0;
    int op_count_odd = 0;
    for (int i = 0; i < s.length(); i++)
    {
        if (i % 2 == 0)
        {
            if (s[i] == '0')
                op_count_even++;
            else
                op_count_odd++;
        }
        else
        {
            if (s[i] == '0')
                op_count_odd++;
            else
                op_count_even++;
        }
    }
    return min(op_count_even, op_count_odd);
}