#include <bits/stdc++.h>
using namespace std;

int leastInterval(vector<char> &tasks, int n)
{
    unordered_map<char, int> mp;
    int count = 0;
    for (auto e : tasks)
    {
        mp[e]++;
        count = max(count, mp[e]);
    }

    int ans = (count - 1) * (n + 1);
    for (auto e : mp)
        if (e.second == count)
            ans++;
    return max((int)tasks.size(), ans);
}

int leastInterval(vector<char> &tasks, int n)
{
    priority_queue<int> pq;  // Max heap to store task frequencies
    queue<vector<int>> q;    // Queue to track idle times
    vector<int> counter(26); // Array to store task frequencies

    // Count the frequency of each task
    for (int i = 0; i < tasks.size(); ++i)
        ++counter[tasks[i] - 'A'];
    // Push nonzero frequencies to max heap
    for (int i = 0; i < 26; ++i)
    {
        if (counter[i])
            pq.push(counter[i]);
    }

    int time = 0; // Initialize time counter
    while (!q.empty() || !pq.empty())
    {           // Continue until both queues are empty
        ++time; // Increment time counter

        // Process tasks from max heap
        if (!pq.empty())
        {
            if (pq.top() - 1)
                q.push({pq.top() - 1, time + n}); // Enqueue with idle time
            pq.pop();                             // Pop the task from max heap
        }

        // Check if any tasks are ready to execute
        if (!q.empty() && q.front()[1] == time)
        {
            pq.push(q.front()[0]); // Push task back to max heap
            q.pop();               // Dequeue the task
        }
    }
    return time; // Return total time elapsed
}

int main()
{
}