#include<bits/stdc++.h>
using namespace std;

string countAndSay(int n) {
    string ans = "1";
    for(int i=1;i<n;i++) {
        char prev = ans[0];
        int carry = 1;
        string curr = "";
        for(int j=1;j<ans.size();j++) {
            if (prev == ans[j]) carry++;
            else {
                curr += to_string(carry) + prev;
                prev = ans[j];
                carry = 1;
            }
        }
        curr += to_string(carry) + prev;
        ans = curr;
    }
    return ans;
}