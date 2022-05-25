#include<bits/stdc++.h>
#include <iostream>
using namespace std;


class twoS {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> indices;
        for (int i = 0; i < nums.size(); i++) {
            if (indices.find(target - nums[i]) != indices.end()) {
                return {indices[target - nums[i]], i};
            }
            indices[nums[i]] = i;
        }
        return {};
    }
};

int main() {
    vector<int> num = {12,45,65,43,23,54,76};
    twoS tws;
    vector<int> ans = tws.twoSum(num, 88);
}

