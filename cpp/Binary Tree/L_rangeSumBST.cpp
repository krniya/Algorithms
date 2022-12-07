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

int rangeSumBST(TreeNode* root, int low, int high) {
    int res = 0;
    preOrder(root, low, high, res);
    return res;
}
void preOrder(TreeNode* root, int low, int high, int &res) {
    if (!root) return;
    preOrder(root->left, low, high, res);
    if(low <= root->val and root->val <= high) res += root->val;
    preOrder(root->right, low, high, res);
}