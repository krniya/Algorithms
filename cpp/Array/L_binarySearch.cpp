#include<bits/stdc++.h>
using namespace std;

int search(vector<int>& nums, int target) {
        int l=0, r=nums.size()-1;
        while(l<r){
            int mid = l + (r-l)/2;
            if(nums[mid] >= target)
                r = mid;
            else
                l = mid + 1;
        }

        if(nums[l] != target) return -1;
        return l;
    }