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

bool isSameTree(TreeNode *p, TreeNode *q)
{
    if (!p && !q)
        return true;
    if (!p || !q)
        return false;
    if (p->val != q->val)
        return false;
    return isSameTree(p->left, q->left) && isSameTree(p->right, q->right);
}

bool isSameTree(TreeNode *p, TreeNode *q)
{
    queue<TreeNode *> queue;
    queue.push(p);
    queue.push(q);

    while (!queue.empty())
    {
        TreeNode *node1 = queue.front();
        queue.pop();
        TreeNode *node2 = queue.front();
        queue.pop();

        if (node1 == NULL && node2 == NULL)
        {
            continue;
        }
        if (node1 == NULL || node2 == NULL)
        {
            return false;
        }
        if (node1->val != node2->val)
        {
            return false;
        }

        queue.push(node1->left);
        queue.push(node2->left);
        queue.push(node1->right);
        queue.push(node2->right);
    }
    return true;
}

int main()
{
}
