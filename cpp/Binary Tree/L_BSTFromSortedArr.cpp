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

TreeNode* sortedArrayToBST(vector<int>& nums) {
    return BSTHelper(0, nums.size() - 1, nums);
}
TreeNode* BSTHelper(int left, int right, vector<int>& nums) {
    if(left>right) return NULL;
    int mid = (left + right + 1) / 2;
    TreeNode *root = new TreeNode(nums[mid]);
    root->left = BSTHelper(left, mid - 1, nums);
    root->right = BSTHelper(mid + 1, right, nums);
    return root;
}

int main() {

}