#include<bits/stdc++.h>
using namespace std;

int maxIceCream(vector<int>& costs, int coins) {
    sort(costs.begin(), costs.end());
    int total = 0;
    for(int price: costs) {
        if (price > coins) return total;
        coins -= price;
        total++;
    }
    return total;
}