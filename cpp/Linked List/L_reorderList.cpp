#include <bits/stdc++.h>

struct ListNode
{
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};

void reorderList(ListNode *head)
{
    ListNode *slow = head;
    ListNode *fast = head->next;
    while (fast && fast->next)
    {
        slow = slow->next;
        fast = fast->next->next;
    }
    ListNode *second = slow->next;
    slow->next = NULL;
    ListNode *prev = NULL;
    while (second)
    {
        ListNode *curr = second;
        second = second->next;
        curr->next = prev;
        prev = curr;
    }
    ListNode *first = head;
    second = prev;
    while (second)
    {
        ListNode *tem1 = first->next, *tem2 = second->next;
        first->next = second;
        second->next = tem1;
        first = tem1;
        second = tem2;
    }
}

void reorderList(ListNode *head)
{
    stack<ListNode *> s;
    ListNode *curr = head;
    while (curr)
    {
        s.push(curr);
        curr = curr->next;
    }
    curr = head;
    unordered_map<ListNode *, bool> vis;
    while (true)
    {
        ListNode *last = s.top();
        s.pop();
        ListNode *next = curr->next;
        vis[curr] = true;
        if (vis[last])
        {
            curr->next = NULL;
            break;
        }
        curr->next = last;
        vis[last] = true;
        curr = curr->next;
        if (vis[next])
        {
            curr->next = NULL;
            break;
        }
        curr->next = next;
        curr = curr->next;
    }
}

int main()
{
}