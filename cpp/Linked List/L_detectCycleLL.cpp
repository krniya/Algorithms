#include<bits/stdc++.h>

struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};
 


bool hasCycle(ListNode *head) {
    if (!head) return false;
    ListNode *fast = head;
    ListNode *slow = head;
    while(fast && fast->next) {
        slow = slow->next;
        fast = fast->next->next;
        if (fast == slow) {
            return true;
        }
    }
    return false;
}



int main() {
    cout << minDistance("sea","eat");

}