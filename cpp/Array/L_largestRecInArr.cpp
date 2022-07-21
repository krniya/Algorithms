#include<bits/stdc++.h>
#include <iostream>
using namespace std;


int largestRectangleArea(vector<int>& heights) {
        stack<pair<int,int>> stack;
        int maxRec = 0, n = heights.size();
        for(int i=0;i<n;i++) {
            int start = i;
            int height = heights[i];
            while(!stack.empty() && stack.top().second > height) {
                pair<int, int> prev = stack.top();
                stack.pop();
                maxRec = max(maxRec, prev.second * (i - prev.first));
                start = prev.first;
            }
            stack.push({start, height});
        }
        while(!stack.empty()) {
            pair<int,int> height = stack.top();
            maxRec = max(maxRec, height.second * (n - height.first));
            stack.pop();
        }
        return maxRec;
    }
    
int main() {
    vector<int> num = {12,45,65,43,23,54,76};
    int n = largestRectangleArea(num);
    cout<<n;
}

