#include<bits/stdc++.h>
using namespace std;

    int maximumUniqueSubarray1(vector<int>& nums) {
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

    int maximumUniqueSubarray(vector<int>& nums) {
        int n = nums.size();
        vector<int> count(1e4+1,0);
        int l=0; int sum = 0; int maxi = INT_MIN;
        for(int i=0;i<n;i++){
            sum += nums[i],count[nums[i]]++;
            while(l<n and count[nums[i]]>1)
                sum -= nums[l],count[nums[l]]--,l++;
            maxi = max(maxi,sum);
        }
        return maxi;
    }

int main() {
    vector<int> nums = {4,2,4,5,6};
    cout << maximumUniqueSubarray(nums);

}