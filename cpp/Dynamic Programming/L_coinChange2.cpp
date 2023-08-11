#include <bits/stdc++.h>
using namespace std;

int change(int amount, vector<int> &coins)
{
    vector<int> changeMethodCount(amount + 1, 0);
    changeMethodCount[0] = 1;
    for (int coin : coins)
    {
        for (int smallAmount = coin; smallAmount <= amount; smallAmount++)
        {
            changeMethodCount[smallAmount] += changeMethodCount[smallAmount - coin];
        }
    }
    return changeMethodCount[amount];
}