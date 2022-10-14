#include<bits/stdc++.h>
using namespace std;

struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(NULL) {}
};
 


ListNode* deleteMiddle(ListNode* head) {
        if(!head->next) return NULL;
        ListNode *slow = head;
        ListNode *fast = head->next;
        while(fast->next and fast->next->next) {
            slow = slow->next;
            fast = fast->next->next;
        }
        slow->next = slow->next->next;
        return head;
    }