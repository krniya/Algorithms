#include<bits/stdc++.h>

struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(NULL) {}
};
 


ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
    ListNode *dummy, *curr = new ListNode();
    dummy = curr;
    int carry = 0;
    while(l1 || l2 || carry) {
        int v1 = (l1 != NULL) ? l1->val : 0;
        int v2 = (l2 != NULL) ? l2->val : 0;
        int val = v1 + v2 + carry;
        carry = val / 10;
        val = val % 10;
        curr->next = new ListNode(val);
        curr = curr->next;
        l1 = (l1 != NULL) ? l1->next : NULL;
        l2 = (l2 != NULL) ? l2->next : NULL;
    }
    return dummy->next;
}


int main() {


}