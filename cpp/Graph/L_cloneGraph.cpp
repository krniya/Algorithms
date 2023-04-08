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
Node* dfs(Node* cur,unordered_map<Node*,Node*>& mp)

    {

        vector<Node*> neighbour;

        Node* clone=new Node(cur->val);

        mp[cur]=clone;

            for(auto it:cur->neighbors)

            {

                if(mp.find(it)!=mp.end())   //already clone and stored in map

                {

                    neighbour.push_back(mp[it]);    //directly push back the clone node from map to neigh

                }

                else

                    neighbour.push_back(dfs(it,mp));

            }

            clone->neighbors=neighbour;

            return clone;

    }

    Node* cloneGraph(Node* node) {

        unordered_map<Node*,Node*> mp;

        if(node==NULL)

            return NULL;

        if(node->neighbors.size()==0)   //if only one node present no neighbors

        {

            Node* clone= new Node(node->val);

            return clone; 

        }

        return dfs(node,mp);

    }


int main() {

}
