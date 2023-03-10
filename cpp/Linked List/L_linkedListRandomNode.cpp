#include<bits/stdc++.h>
using namespace std;

struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};

class LinkedListRandom
{
    vector<int> v;
    int n;

public:
    LinkedListRandom(ListNode *head)
    {
        ListNode *ptr = head;
        while (ptr)
        {
            v.push_back(ptr->val);
            ptr = ptr->next;
        }
        n = v.size();
    }

    int getRandom()
    {
        static int i = 0;
        if (i == 0)
        {
            srand(time(NULL));
            i++;
        }
        return v[rand() % n];
    }
};