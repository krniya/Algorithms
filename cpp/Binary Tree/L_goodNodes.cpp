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

int goodNodes(TreeNode* root) {
    int res = 0;
    dfs(root, root->val, res);
    return res;
}
void dfs(TreeNode* root, int maxN, int& res) {
    if(!root) return;
    if(root->val >= maxN) res++;
    maxN = max(maxN, root->val);
    dfs(root->left, maxN, res);
    dfs(root->right, maxN, res);
}
int main() {

}