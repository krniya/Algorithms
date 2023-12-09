#include <bits/stdc++.h>
using namespace std;

struct TreeNode
{
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

vector<int> inorderTraversal(TreeNode *root)
{
    vector<int> result;
    helper(root, result);
    return result;
}

void helper(TreeNode *root, vector<int> &result)
{
    if (root != nullptr)
    {
        helper(root->left, result);
        result.push_back(root->val);
        helper(root->right, result);
    }
}