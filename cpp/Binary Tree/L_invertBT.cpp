#include<bits/stdc++.h>
using namespace std;

TreeNode* invertTree(TreeNode* root) {
        if (!root) return 0;
        TreeNode* tmp = root->left;
        root->left = root->right;
        root->right = tmp;
        invertTree(root->left);
        invertTree(root->right);
        return root;
}

TreeNode* invertTree2(TreeNode* root) {
        if(!root) return root;
        queue<TreeNode*> q;
        q.push(root);
        while(q.size()) {
            TreeNode* curr = q.front();
            q.pop();
            swap(curr->left, curr->right);
            if(curr->left) q.push(curr->left);
            if(curr->right) q.push(curr->right);
        }
        return root;
    }

int main() {

}