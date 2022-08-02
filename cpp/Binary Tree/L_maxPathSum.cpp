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

int maxPathSum(TreeNode* root) {
    int res = root->val;
    dfs(root, res);
    return res;
}
int dfs(TreeNode* root, int& res) {
    if(!root) return 0;
    int leftmax = max(0, dfs(root->left, res));
    int rightmax = max(0, dfs(root->right, res));
    res = max(res, root->val + leftmax + rightmax);
    return root->val + max(leftmax, rightmax);
}

int main() {

}