#include <bits/stdc++.h>
using namespace std;

vector<unordered_set<int>> tree;
vector<int> res, count;
vector<int> sumOfDistancesInTree(int N, vector<vector<int>> &edges)
{
    tree.resize(N);
    res.assign(N, 0);
    count.assign(N, 1);
    for (auto e : edges)
    {
        tree[e[0]].insert(e[1]);
        tree[e[1]].insert(e[0]);
    }
    dfs(0, -1);
    dfs2(0, -1);
    return res;
}
void dfs(int root, int pre)
{
    for (auto i : tree[root])
    {
        if (i == pre)
            continue;
        dfs(i, root);
        count[root] += count[i];
        res[root] += res[i] + count[i];
    }
}
void dfs2(int root, int pre)
{
    for (auto i : tree[root])
    {
        if (i == pre)
            continue;
        res[i] = res[root] - count[i] + count.size() - count[i];
        dfs2(i, root);
    }
}

class Solution
{
private:
    std::vector<std::vector<int>> graph;
    std::vector<int> count;
    std::vector<int> res;
    int N;

public:
    std::vector<int> sumOfDistancesInTree(int N, std::vector<std::vector<int>> &edges)
    {
        this->N = N;
        res.resize(N);
        graph.resize(N);
        count.resize(N);

        for (auto &e : edges)
        {
            ++count[e[0]];
            ++count[e[1]];
        }
        for (int i = 0; i < N; i++)
        {
            graph[i].resize(count[i]);
        }
        for (auto &e : edges)
        {
            graph[e[0]][--count[e[0]]] = e[1];
            graph[e[1]][--count[e[1]]] = e[0];
        }
        dfs1(0, -1);
        dfs2(0, -1);
        return res;
    }

private:
    void dfs1(int cur, int parent)
    {
        count[cur] = 1;
        for (int child : graph[cur])
        {
            if (child != parent)
            {
                dfs1(child, cur);
                count[cur] += count[child];
                res[cur] += res[child] + count[child];
            }
        }
    }

    void dfs2(int cur, int parent)
    {
        for (int child : graph[cur])
        {
            if (child != parent)
            {
                res[child] = res[cur] + N - 2 * count[child];
                dfs2(child, cur);
            }
        }
    }
};
