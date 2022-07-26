#include<bits/stdc++.h>

struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};
 


ListNode* reverseList(ListNode* head) {
        ListNode* prev = NULL;
        while (head) {
            ListNode *curr = head;
            head = head->next;
            curr->next = prev;
            prev = curr;
        }
        return prev;
    }


int main() {

}