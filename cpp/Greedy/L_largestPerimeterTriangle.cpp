#include<bits/stdc++.h>
using namespace std;

int largestPerimeter(vector<int>& A) {
    sort(A.begin(), A.end());
    for (int i = A.size() - 1 ; i > 1; --i)
        if (A[i] < A[i - 1] + A[i - 2])
            return A[i] + A[i - 1] + A[i - 2];
    return 0;
}