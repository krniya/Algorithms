#include<bits/stdc++.h>
using namespace std;

struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(NULL) {}
};

ListNode* swapNodes(ListNode* head, int k) {
    ListNode *slow = head, *fast = head, *first;
    int temp;
    for (int i=0;i<k-1;i++) fast = fast->next;
    first = fast;
    while(fast->next) {
        fast = fast->next;
        slow = slow->next;
    }
    temp = first->val;
    first->val = slow->val;
    slow->val = temp;
    return head;
}