#include<bits/stdc++.h>
using namespace std;

vector<vector<int>> threeSum(vector<int>& nums) {
    sort(nums.begin(), nums.end());
    vector<vector<int>> res;
    for(int i=0;i<nums.size()-2;i++) {
        if (i>0 and nums[i] == nums[i-1]) continue;
        int l = i + 1;
        int r = nums.size() - 1;
        while (l<r) {
            int curr = nums[i] + nums[l] + nums[r];
            if (curr == 0) {
                res.push_back({nums[i],nums[l],nums[r]});
                while (l<r && nums[l]==nums[l+1]) l++;
                while (l<r && nums[r]==nums[r-1]) r--;
                l++;
                r--;
            }
            else if (curr > 0) r--;
            else if (curr < 0) l++;
        }
    }
    return res;
}

int main() {
	vector<int> nums = {-1,0,1,2,-1,-4};
	vector<vector<int>> res;
	res = threeSum(nums);
	for (auto n:res) {
		for (auto m:n) {
			cout<<m;
		}
		cout<<endl;
	}
}