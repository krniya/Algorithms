#include<bits/stdc++.h>
using namespace std;

ool containsDuplicate(vector<int>& nums) {
    set<int> mySet;
    for (auto& num: nums) {
        if (mySet.find(num) != mySet.end())
            return true;
        mySet.insert(num);
    }
    return false;
}

int main() {

}