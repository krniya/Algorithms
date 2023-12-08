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

string tree2str(TreeNode *root)
{
    string str = "";
    check(root, str);
    return str;
}
void check(TreeNode *root, string &str)
{
    if (root == NULL)
    {
        return;
    }
    str += to_string(root->val);
    if (root->left || root->right)
    {
        str += '(';
        check(root->left, str);
        str += ')';
    }
    if (root->right)
    {
        str += '(';
        check(root->right, str);
        str += ')';
    }
}