#include<bits/stdc++.h>
using namespace std;

int maxProfit(vector<int>& prices) {
    int minValue = prices[0];
    int maxDiff = 0;
    for (int i = 1; i < prices.size(); i++) {
        minValue = min(minValue, prices[i]);
        maxDiff = max(maxDiff, prices[i] - minValue);
    }
    return maxDiff;
}

int main() {

}