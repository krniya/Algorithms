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

bool findTarget(TreeNode* root, int k) {
    unordered_set <int> visit;
    return dfs(root, k, visit);
}

bool dfs(TreeNode* node, int k, unordered_set <int> &visit) {
    if (!node) return false;
    if (visit.find(k - node->val) != visit.end()) return true;
    else visit.insert(node->val);
    return dfs(node->left, k, visit) or dfs(node->right, k, visit);
}