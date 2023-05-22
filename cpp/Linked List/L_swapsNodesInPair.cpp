#include <bits/stdc++.h>
using namespace std;

struct ListNode
{
    string val;
    ListNode *next;
    ListNode *prev;
    ListNode() : val(""), next(nullptr), prev(nullptr) {}
    ListNode(string x) : val(x), next(NULL), prev(NULL) {}
};

ListNode *swapPairs(ListNode *head)
{
    if (head == NULL || head->next == NULL)
    {
        return head;
    }

    ListNode *temp;    // temporary pointer to store head -> next
    temp = head->next; // give temp what he want

    head->next = swapPairs(head->next->next); // changing links
    temp->next = head;                        // put temp -> next to head

    return temp;
}