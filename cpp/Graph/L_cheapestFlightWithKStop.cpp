#include<bits/stdc++.h>
using namespace std;

int findCheapestPrice(int n, vector<vector<int>>& a, int src, int sink, int k) {
    vector<int> c(n, 1e8);
    c[src] = 0;
    
    for(int z=0; z<=k; z++){
        vector<int> C(c);
        for(auto e: a)
            C[e[1]] = min(C[e[1]], c[e[0]] + e[2]);
        c = C;
    }
    return c[sink] == 1e8 ? -1 : c[sink];
}

int findCheapestPrice(int n, vector<vector<int>> &flights, int src, int dst, int k)
{
    unordered_map<int, vector<pair<int, int>>> adj;
    for (auto &flight : flights)
    {
        adj[flight[0]].push_back({flight[1], flight[2]});
    }

    vector<int> dist(n, INT_MAX);
    dist[src] = 0;

    queue<pair<int, int>> q;
    q.push({src, 0});
    int stops = 0;

    while (!q.empty() && stops <= k)
    {
        int sz = q.size();
        while (sz-- > 0)
        {
            auto [node, distance] = q.front();
            q.pop();

            if (!adj.count(node))
                continue;

            for (auto &[neighbour, price] : adj[node])
            {
                if (price + distance >= dist[neighbour])
                    continue;
                dist[neighbour] = price + distance;
                q.push({neighbour, dist[neighbour]});
            }
        }
        stops++;
    }
    return dist[dst] == INT_MAX ? -1 : dist[dst];
}