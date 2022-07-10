#include<bits/stdc++.h>
using namespace std;

int maxArea(vector<int>& height) {
    int left = 0, right = height.size() - 1;
    int maxWater = 0;
    while(left<right) {
        int currMax = min(height[left], height[right]) * (right-left);
        maxWater = max(maxWater, currMax);
        if(height[left]<height[right]) left++;
        else right--;
    }
    return maxWater;
}

int main() {
    vector<int> hei = {1,8,6,2,5,4,8,3,7};
    cout<<maxArea(hei);
}