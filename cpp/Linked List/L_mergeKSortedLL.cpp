#include<bits/stdc++.h>
using namespace std;

struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(NULL) {}
};
 
ListNode* mergeKLists(vector<ListNode*>& lists) {
    vector<int>v;
    for(int i=0;i<lists.size();i++){
        while(lists[i]){
            v.push_back(lists[i]->val);
            lists[i]=lists[i]->next;
        }
    }
    sort(rbegin(v),rend(v));
    ListNode* ans=nullptr;
    for(int i=0;i<v.size();i++){
        ans=new ListNode(v[i],ans);
    }
    return ans;
}