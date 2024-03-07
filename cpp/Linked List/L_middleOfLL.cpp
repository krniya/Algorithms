#include <bits/stdc++.h>
using namespace std;

struct ListNode
{
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(NULL) {}
};

ListNode *middleNode(ListNode *head)
{
    ListNode *slow = head;
    ListNode *fast = head;
    while (fast and fast->next)
    {
        slow = slow->next;
        fast = fast->next->next;
    }
    return slow;
}

int listLength(ListNode *head)
{
    int len = 0;
    while (head != NULL)
    {
        len++;
        head = head->next;
    }
    return len;
}

ListNode *middleNode(ListNode *head)
{
    int len = listLength(head);
    int middle = len / 2;
    ListNode *temp = head;
    int count = 0;
    while (count < middle)
    {
        temp = temp->next;
        count++;
    }
    return temp;
}