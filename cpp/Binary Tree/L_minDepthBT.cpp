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

/**
 * The function `minDepth` calculates the minimum depth of a binary tree using a breadth-first search
 * algorithm.
 *
 * @param root The root parameter is a pointer to the root node of a binary tree.
 *
 * @return the minimum depth of a binary tree.
 */
int minDepth(TreeNode *root)
{
    if (root == NULL)
        return 0;

    queue<TreeNode *> q;
    q.push(root);
    int depth = 0;

    while (!q.empty())
    {
        int size = q.size();
        depth++;

        for (int i = 0; i < size; i++)
        {
            TreeNode *node = q.front();
            q.pop();

            if (node->left == NULL && node->right == NULL)
                return depth;

            if (node->left)
                q.push(node->left);

            if (node->right)
                q.push(node->right);
        }
    }

    return 0;
}