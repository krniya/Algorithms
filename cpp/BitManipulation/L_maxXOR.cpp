#include<bits/stdc++.h>
using namespace std;
int maximumXOR(vector<int>& nums) {
        int res = 0;
        for (int a : nums)
            res |= a;
        return res;
    }
int main() {
    cout << minDistance("sea","eat");

}