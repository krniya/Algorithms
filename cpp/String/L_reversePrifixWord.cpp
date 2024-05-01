#include <bits/stdc++.h>
using namespace std;

string reversePrefix(string word, char ch)
{
    int j = word.find(ch);
    if (j != -1)
    {
        reverse(word.begin(), word.begin() + j + 1);
    }
    return word;
}