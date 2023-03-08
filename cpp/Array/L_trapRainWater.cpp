
#include<bits/stdc++.h>
using namespace std;

int trap(vector<int>& height) {
    int i = 0;
    int j = height.size() - 1;
    
    int maxLeft = height[i];
    int maxRight = height[j];
    
    int result = 0;
    
    while (i < j) {
        if (maxLeft <= maxRight) {
            i++;
            maxLeft = max(maxLeft, height[i]);
            result += maxLeft - height[i];
        } else {
            j--;
            maxRight = max(maxRight, height[j]);
            result += maxRight - height[j];
        }
    }
    
    return result;
}

int trap(vector<int>& height) {
        int n = height.size();
        vector<int> leftMax(n), rightMax(n);
        for (int i = 1; i < n; ++i) 
            leftMax[i] = max(height[i-1], leftMax[i-1]);
        for (int i = n-2; i >= 0; --i) 
            rightMax[i] = max(height[i+1], rightMax[i+1]);
        
        int ans = 0;
        for (int i = 0; i < n; ++i) {
            int waterLevel = min(leftMax[i], rightMax[i]);
            if (waterLevel >= height[i]) ans += waterLevel - height[i];
        }
        return ans;
    }

int main() {

}

