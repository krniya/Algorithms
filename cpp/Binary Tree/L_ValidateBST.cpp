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

bool isValidBST(TreeNode* root) {
    return validateBST(root, LONG_MAX, LONG_MIN);
}
bool validateBST(TreeNode* root, long maxN, long minN) {
    if(!root) return true;
    if(root->val >= maxN || root->val <= minN) return false;
    return validateBST(root->left, root->val, minN) && validateBST(root->right, maxN, root->val);
}
int main() {

}