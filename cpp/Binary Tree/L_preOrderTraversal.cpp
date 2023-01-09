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

vector<int> preorderTraversal(TreeNode* root) {
        vector<int> res;
        preOrd(root, res);
        return res;
        
    }
    void preOrd(TreeNode* root, vector<int> &res) {
        if (!root) return;
        res.push_back(root->val);
        preOrd(root->left, res);
        preOrd(root->right, res);
    }