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

void reverse(ListNode* &head,ListNode* &prev){

        if(head==NULL ) return ;

        ListNode* curr =head;
        ListNode* forward;
        
        if(curr!=NULL){
        forward=curr->next;
        curr->next=prev;
        prev=curr;
        curr=forward;
    }

        reverse(forward,prev);

    }
    ListNode* reverseList(ListNode* head) {

        ListNode* prev =NULL;
        

        reverse(head,prev);
        return prev;
        
    }

int main() {

}
