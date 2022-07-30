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

int diameterOfBinaryTree(TreeNode* root) {
    int res = 0;
    dfs(root, res);
    return res;
}

int dfs(TreeNode* root, int& res) {
    if(!root) return 0;
    int left = dfs(root->left, res);
    int right = dfs(root->right, res);
    res = max(res, left + right);
    return 1 + max(left, right);
}
int main() {

}

