#include<bits/stdc++.h>

struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};

ListNode *detectCycle(ListNode *head) {
    ListNode *slow = head, *fast = head;
    while(fast  and fast->next) {
        slow = slow->next;
        fast = fast->next->next;
        if(fast == slow) {
            slow = head;
            while(slow!=fast) {
                slow = slow->next;
                fast = fast->next;
            }
            return slow;
        }
    }
    return NULL;
}