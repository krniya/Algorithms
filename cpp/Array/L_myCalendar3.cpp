#include<bits/stdc++.h>
using namespace std;


map<int, int> timeline;

    int book(int s, int e) {
        timeline[s]++; // 1 new event will be starting at [s]
        timeline[e]--; // 1 new event will be ending at [e];
        int ongoing = 0, k = 0;
        for (pair<int, int> t : timeline)
            k = max(k, ongoing += t.second);
        return k;
    }