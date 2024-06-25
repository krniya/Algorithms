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

int sum = 0;

void traverse(TreeNode *root)
{
    if (root)
    {
        traverse(root->right); // Traverse the right subtree
        sum += root->val;      // Update the sum
        root->val = sum;       // Update the current node's value
        traverse(root->left);  // Traverse the left subtree
    }
}

TreeNode *bstToGst(TreeNode *root)
{
    traverse(root);
    return root;
}