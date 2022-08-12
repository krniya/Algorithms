#include<bits/stdc++.h>
using namespace std;

class Node {
public:
    int val;
    vector<Node*> neighbors;
    Node() {
        val = 0;
        neighbors = vector<Node*>();
    }
    Node(int _val) {
        val = _val;
        neighbors = vector<Node*>();
    }
    Node(int _val, vector<Node*> _neighbors) {
        val = _val;
        neighbors = _neighbors;
    }
};
unordered_map<Node*, Node*> m;
Node* cloneGraph(Node* node) {
    if (node == NULL) {
        return NULL;
    }
    
    Node* copy = new Node(node->val);
    m[node] = copy;
    
    queue<Node*> q;
    q.push(node);
    
    while (!q.empty()) {
        Node* curr = q.front();
        q.pop();
        
        for (int i = 0; i < curr->neighbors.size(); i++) {
            Node* neighbor = curr->neighbors[i];
            
            if (m.find(neighbor) == m.end()) {
                m[neighbor] = new Node(neighbor->val);
                q.push(neighbor);
            }
            
            m[curr]->neighbors.push_back(m[neighbor]);
        }
    }
    return copy;
}

int main() {

}