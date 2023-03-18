#include<bits/stdc++.h>
using namespace std;

struct listnode {
    string val;
    listnode *next;
    listnode *prev;
    listnode() : val(""), next(nullptr), prev(nullptr) {}
    listnode(string x) : val(x), next(NULL), prev(NULL) {}
};

class BrowserHistory {
public:
    listnode *curr;
    BrowserHistory(string homepage) {
        curr = new listnode(homepage);

    }
    
    void visit(string url) {
        curr->next = nullptr;
        listnode *newPage = new listnode(url);
        curr->next = newPage;
        newPage->prev = curr;
        curr = newPage;
    }
    
    string back(int steps) {
        while(curr->prev and steps--) {
            curr = curr->prev;
        }
        return curr->val;
    }
    
    string forward(int steps) {
        while(curr->next and steps--) {
            curr = curr->next;
        }
        return curr->val;
    }
};

