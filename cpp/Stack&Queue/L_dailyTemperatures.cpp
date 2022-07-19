#include<bits/stdc++.h>
using namespace std;

vector<int> dailyTemperatures(vector<int>& temperatures) {
    int n = temperatures.size();
    stack<pair<int,int>> stack;
    vector<int> res(n);
    for(int i=0;i<n;i++) {
        while(!stack.empty() && temperatures[i] > stack.top().first) {
            int prevIdx  = stack.top().second;
            stack.pop();
            res[prevIdx] = i - prevIdx;
        }
        stack.push({temperatures[i], i});
    }
    return res;
}

int main() {

}