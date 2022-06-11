#include<bits/stdc++.h>
using namespace std;

    vector<int> successfulPairs(vector<int>& spells, vector<int>& potions, long long success) {
        sort(potions.begin(), potions.end());
        vector<int> res;
        for (int a: spells) {
            long need = (success + a - 1) / a;
            auto it = lower_bound(potions.begin(), potions.end(), need);
            res.push_back(potions.end() - it);
        }
        return res;
    }

int main() {
    vector<int> s = {5,1,3};
    vector<int> p = {1,2,3,4,5};
    int suc = 7;
    vector<int> a = successfulPairs(s,p,suc);
}