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



bool isSubtree(TreeNode* root, TreeNode* subRoot) {
    if(!subRoot) return true;
    if(!root) return false;
    if(isMatch(root, subRoot)) return true;
    return isSubtree(root->left, subRoot) || isSubtree(root->right, subRoot);
}

bool isMatch(TreeNode* root, TreeNode* subRoot) {
    if (!root && !subRoot) return true;
    if (root && subRoot && root->val == subRoot->val)
        return isMatch(root->left, subRoot->left) && isMatch(root->right, subRoot->right);
    return false;
}
int main() {

}

