#include<bits/stdc++.h>
using namespace std;

struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(NULL) {}
};
 

ListNode* oddEvenList(ListNode* head) {
    if(!head) return NULL;
    ListNode* odd = head;
    ListNode* even = head->next;
    ListNode* evenHead = even;
    while(even and even->next) {
        odd->next = odd->next->next;
        even->next = even->next->next;
        odd = odd->next;
        even = even->next;
    }
    odd->next = evenHead;
    return head;
}