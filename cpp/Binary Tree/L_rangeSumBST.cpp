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

int rangeSumBST(TreeNode *root, int low, int high)
{
    int res = 0;
    preOrder(root, low, high, res);
    return res;
}
void preOrder(TreeNode *root, int low, int high, int &res)
{
    if (!root)
        return;
    preOrder(root->left, low, high, res);
    if (low <= root->val and root->val <= high)
        res += root->val;
    preOrder(root->right, low, high, res);
}

int rangeSumBST(TreeNode *root, int low, int high)
{
    if (!root)
        return NULL;
    int count = 0;
    queue<TreeNode *> q;

    q.push(root);

    while (!q.empty())
    {
        int n = q.size();
        for (int i = 0; i < n; i++)
        {
            TreeNode *curr = q.front();
            q.pop();
            if (curr->val >= low && curr->val <= high)
            {
                count += curr->val;
            }
            if (curr->left)
                q.push(curr->left);
            if (curr->right)
                q.push(curr->right);
        }
    }

    return count;
}