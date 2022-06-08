#include<bits/stdc++.h>
using namespace std;

int maxDepthRec(TreeNode* root) {
        if(!root) return 0;
        int left = maxDepth(root->left);
        int right = maxDepth(root->right);
        return max(left, right) + 1;
}
int maxDepthEtr(TreeNode* root) {
        if(!root) return 0;
        int depth = 0;
        queue<TreeNode*> q;
        q.push(root);
        while(!q.empty()) {
            int n = q.size();
            while(n--) {
                TreeNode* curr = q.front();
                q.pop();
                if(curr->left) q.push(curr->left);
                if(curr->right) q.push(curr->right);
            }
            depth++;
        }
        return depth;
    }
int main() {

}