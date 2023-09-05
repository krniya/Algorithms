#include <bits/stdc++.h>
using namespace std;

struct ListNode
{
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(NULL) {}
};

Node *copyRandomList(Node *head)
{
    if (!head)
        return nullptr;

    unordered_map<Node *, Node *> old_to_new;

    Node *curr = head;
    while (curr)
    {
        old_to_new[curr] = new Node(curr->val);
        curr = curr->next;
    }

    curr = head;
    while (curr)
    {
        old_to_new[curr]->next = old_to_new[curr->next];
        old_to_new[curr]->random = old_to_new[curr->random];
        curr = curr->next;
    }

    return old_to_new[head];
}