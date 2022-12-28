#include<bits/stdc++.h>
using namespace std;

int minStoneSum(vector<int>& A, int k) {
    priority_queue<int> pq(A.begin(), A.end());
    int res = accumulate(A.begin(), A.end(), 0);
    while (k--) {
        int a = pq.top();
        pq.pop();
        pq.push(a - a / 2);
        res -= a / 2;
    }
    return res;
}