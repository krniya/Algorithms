#include<bits/stdc++.h>
using namespace std;
int wiggleMaxLength(vector<int>& nums) {
    int pos = 1, neg = 1;
    for(int i=1;i<nums.size();i++) {
        if (nums[i-1] > nums[i]) {
            neg = pos + 1;
        } else if (nums[i-1] < nums[i]) {
            pos = neg + 1;
        }
    }
    return max(neg,pos);
}
int main() {

}