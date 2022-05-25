#include<bits/stdc++.h>
using namespace std;

int maxSubArr(int nums[]) {
    int currSum = nums[0];
    int maxSum = nums[0];
    int n = sizeof(nums);
    for (int i = 1; i < n; i++) {
        currSum = max(nums[i], nums[i] + currSum);
        maxSum = max(maxSum, currSum);
    }
    return maxSum;
}

int main() {
    int nums[] = {-2,1,-3,4,-1,2,1,-5,4};
    int res = maxSubArr(nums);
    cout << res;
}