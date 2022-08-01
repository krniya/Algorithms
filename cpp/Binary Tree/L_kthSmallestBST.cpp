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

int kthSmallest(TreeNode* root, int k) {
    int res=0;
    inord(root,k,res);
    return res;
}
void inord(TreeNode* root, int& k, int& res) {
    if(!root) return;
    inord(root->left,k,res);
    k--;
    if(k==0) {
        res = root->val;
        return;
    }
    inord(root->right,k,res);
}
int main() {

}