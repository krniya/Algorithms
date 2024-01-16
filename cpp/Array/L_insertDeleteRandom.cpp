#include <bits/stdc++.h>
using namespace std;

class RandomizedSet
{
private:
    vector<int> a;
    unordered_map<int, int> m;

public:
    RandomizedSet()
    {
    }

    bool insert(int val)
    {
        if (m.find(val) != m.end())
            return false;
        else
        {
            a.push_back(val);
            m[val] = a.size() - 1;
            return true;
        }
    }

    bool remove(int val)
    {
        if (m.find(val) == m.end())
            return false;
        else
        {
            int last = a.back();
            a[m[val]] = a.back();
            a.pop_back();
            m[last] = m[val];
            m.erase(val);
            return true;
        }
    }

    int getRandom()
    {
        return a[rand() % a.size()];
    }
};

class RandomizedSet
{
    unordered_map<int, int> S;
    vector<int> idx;
    int sz = 0;
    mt19937 rng; // Mersenne Twister random number engine
public:
    RandomizedSet()
    {
        rng = mt19937(time(NULL));
    }

    bool insert(int val)
    {
        if (S.count(val))
            return 0;

        S[val] = sz++;
        idx.push_back(val);
        return 1;
    }

    bool remove(int val)
    {
        if (!S.count(val))
            return 0;

        int r = idx.back();
        int pos = S[val];

        S[r] = pos;
        idx[pos] = r;

        S.erase(val);
        idx.pop_back();
        sz--;

        return 1;
    }
    int getRandom()
    {
        return idx[rng() % sz];
    }
};

auto init = []()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    return 'c';
}();