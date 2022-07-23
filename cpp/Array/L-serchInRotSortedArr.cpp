#include<bits/stdc++.h>
using namespace std;

int search(vector<int>& nums, int target) {
    int left = 0, right = nums.size() - 1;
    while (left <= right) {
        int mid = (left + right) / 2;
        if(nums[mid] == target) return mid;
        if(nums[left] <= nums[mid])
            if(nums[left] <= target && target <= nums[mid]) right = mid - 1;
            else left = mid + 1;
        else
            if(nums[mid] <= target && target <= nums[right]) left = mid + 1;
            else right = mid - 1;
    }
    return -1;
}

int main() {

}