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


bool isBalanced(TreeNode* root) {
    return dfs(root).first;
}

pair<bool,int> dfs(TreeNode* root) {
    if(!root) return {true, 0};
    pair<bool,int> left = dfs(root->left);
    pair<bool,int> right = dfs(root->right);
    bool bal = left.first and right.first and abs(left.second - right.second) <= 1;
    return {bal, 1 + max(left.second, right.second)};
}

int main() {

}

