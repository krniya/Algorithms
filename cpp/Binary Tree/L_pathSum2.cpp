#include <bits/stdc++.h>
using namespace std;

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

vector<vector<int>> pathSum(TreeNode* root, int targetSum) {
    vector<vector<int>> res;
    vector<int> path;
    dfs(root, res, path, targetSum);
    return res;
}

void dfs(TreeNode* root, vector<vector<int>>& res, vector<int>& path, int target ) {
    if(!root) return;
    path.push_back(root->val);
    if(!root->left and !root->right and target == root->val) res.push_back(path);
    dfs(root->left, res, path, target - root->val);
    dfs(root->right, res, path, target - root->val);
    path.pop_back();
}