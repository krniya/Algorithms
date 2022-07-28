#include<bits/stdc++.h>
using namespace std;
int findDuplicate(vector<int>& nums) {
        int slow = 0, fast = 0;
        do {
            slow = nums[slow];
            fast = nums[nums[fast]];
        } while (slow != fast);
        int slow1 = 0;
        do {
            slow = nums[slow];
            slow1 = nums[slow1];
        } while( slow != slow1);
        return slow;
    }
int main() {

}