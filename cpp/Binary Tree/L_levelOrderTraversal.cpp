#include<bits/stdc++.h>
using namespace std;


struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 };

vector<vector<int>> levelOrder(TreeNode* root) {
    queue<TreeNode*> q;
    q.push(root);
    vector<vector<int>> res;
    if (!root) return res;
    while (q.size()) {
        int siz = q.size();
        vector<int> lvl = {};
        for(int i=0;i<siz;i++) {
            TreeNode* curr = q.front();
            q.pop();
            if (curr->left) q.push(curr->left);
            if (curr->right) q.push(curr->right);
            lvl.push_back(curr->val);
        }
        res.push_back(lvl);
    }
    return res;
}

int main() {

}