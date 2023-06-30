#include <bits/stdc++.h>
using namespace std;

int distributeCookies(std::vector<int> &cookies, int k)
{
    int minUnfairness = std::numeric_limits<int>::max();
    std::vector<int> distribution(k, 0);

    backtrack(cookies, k, 0, minUnfairness, distribution);

    return minUnfairness;
}

void backtrack(const std::vector<int> &cookies, int k, int i, int &minUnfairness, std::vector<int> &distribution)
{
    if (i == cookies.size())
    {
        minUnfairness = std::min(minUnfairness, getMax(distribution));
        return;
    }

    if (minUnfairness <= getMax(distribution))
    {
        return;
    }

    for (int j = 0; j < k; j++)
    {
        distribution[j] += cookies[i];
        backtrack(cookies, k, i + 1, minUnfairness, distribution);
        distribution[j] -= cookies[i];
    }
}

int getMax(const std::vector<int> &distribution)
{
    int max = std::numeric_limits<int>::min();
    for (int num : distribution)
    {
        max = std::max(max, num);
    }
    return max;
}