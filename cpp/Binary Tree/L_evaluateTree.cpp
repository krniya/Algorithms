#include<bits/stdc++.h>
using namespace std;

bool evaluateTree(TreeNode* root) {
    if(root->val == 0) return false;
    if(root->val == 1) return true;
    if(root->val == 2) return evaluateTree(root->left) || evaluateTree(root->right);
    if(root->val == 3) return evaluateTree(root->left) && evaluateTree(root->right);
    return NULL;
}

int main() {

}