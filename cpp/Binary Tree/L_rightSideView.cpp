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

vector<int> traverse(TreeNode* node, vector<int> res, int depth) {
    if(node==NULL) return res;
    if(res.size()==depth) res.push_back(node->val);
    res = traverse(node->right, res, depth + 1);
    res = traverse(node->left,  res, depth + 1);
    return res;
}

vector<int> rightSideView(TreeNode* root) {
    vector<int> res;
    res = traverse(root, res, 0);
    return res;
}

int main() {

}

