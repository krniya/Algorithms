#include<bits/stdc++.h>

struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(NULL) {}
};
 


ListNode* removeNthFromEnd(ListNode* head, int n) {
    ListNode *first = head, *second = head;
    while(n) {
        second = second->next;
        n--;
    }
    if(!second) return head->next;
    while(second->next) {
        first = first->next;
        second = second->next;
    }
    first->next = first->next->next;
    return head;
}


int main() {


}