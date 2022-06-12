#include<bits/stdc++.h>
using namespace std;

    int maximumUniqueSubarray(vector<int>& nums) {
        int l =0, r=0, res = 0, tsum=0, n = nums.size();
        set<int> visit;
        while(r<n) {
            if(visit.find(nums[r]) == visit.end()) {
                tsum += nums[r];
                visit.insert(nums[r]);
                res = max(res, tsum);
                r++;
            } else {
                tsum -= nums[l];
                visit.erase(nums[l]);
                l++;
            }
        }
        return res;
    }

int main() {
    vector<int> nums = {4,2,4,5,6};
    cout << maximumUniqueSubarray(nums);

}