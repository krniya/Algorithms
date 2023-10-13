#include <bits/stdc++.h>
using namespace std;

int minCostClimbingStairs(vector<int> &cost)
{
    int downOne = 0;
    int downTwo = 0;
    for (int i = 2; i <= cost.size(); i++)
    {
        int temp = downOne;
        downOne = min(downOne + cost[i - 1], downTwo + cost[i - 2]);
        downTwo = temp;
    }
    return downOne;
}

int minCostClimbingStairs(vector<int> &cost)
{
    for (int i = 2; i < cost.size(); i++)
    {
        cost[i] += min(cost[i - 1], cost[i - 2]);
    }
    return min(cost[cost.size() - 1], cost[cost.size() - 2]);
}

int main()
{
}