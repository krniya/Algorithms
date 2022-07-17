#include<bits/stdc++.h>
using namespace std;

vector<int> maxSlidingWindow(vector<int>& nums, int k) {
    deque<int> queue;
    vector<int> result;
    int left = 0, right = 0;
    while ( right < nums.size()) {
        while (!queue.empty() && nums[queue.back()] < nums[right]) queue.pop_back();
        queue.push_back(right);
        if (left > queue.front()) queue.pop_front();
        if (right + 1 >= k) {
            result.push_back(nums[queue.front()]);
            left++;
        }
        right++;
    }
    return result;
}

int main() {

}