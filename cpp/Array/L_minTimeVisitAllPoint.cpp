#include <bits/stdc++.h>
using namespace std;

int minTimeToVisitAllPoints(vector<vector<int>> &points)
{
    int total_time = 0, x, y;
    for (int i = 0; i < points.size() - 1; i++)
    {
        x = abs(points[i][0] - points[i + 1][0]);
        y = abs(points[i][1] - points[i + 1][1]);
        total_time += max(x, y);
    }
    return total_time;
}