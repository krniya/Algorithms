#include<bits/stdc++.h>
using namespace std;

vector<int> NGE(vector<int> nums) {
    vector<int> nge(nums.size());
    stack<int> st;
    for (int i=0; i<nums.size();i++) {
        while(!st.empty() && mums[i] > nums[st.top()]) {
            nge[st.top()] = i;
            st.pop();
        }
        st.push(i);
    }
    while(!st.empty()) {
        nge[st.pop()] = -1;
        st.pop();
    }
    return nge;
}

int main() {
    vector<int> nums = {4,5,2,25,7,8};
    vector<int> nge = NGE(nums);
    for(int i=0;i<nge.size();++i) {
        cout<<nge[i];
    }
}