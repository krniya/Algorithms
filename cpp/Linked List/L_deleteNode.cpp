#include<bits/stdc++.h>
using namespace std;

struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(NULL) {}
};
 


void deleteNode(ListNode* node) {
    node->val = node->next->val;
    node->next = node->next->next;
}