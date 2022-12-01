#include<bits/stdc++.h>
using namespace std;

bool halvesAreAlike(string S) {
    string vowels = "aeiouAEIOU";
    int mid = S.size() / 2, ans = 0;
    for (int i = 0, j = mid; i < mid; i++, j++) {
        if (~vowels.find(S[i])) ans++;
        if (~vowels.find(S[j])) ans--;
    }
    return ans == 0;
}