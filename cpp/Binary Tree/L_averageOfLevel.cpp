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

vector<double> averageOfLevels(TreeNode* root) {
    queue<TreeNode*> q;
    vector<double> res;
    q.push(root);
    while (!q.empty()) {
        int n = q.size();
        double total = 0;
        for(int i=0;i<n;i++) {
            TreeNode *curr = q.front();
            q.pop();
            if(curr->left) q.push(curr->left);
            if(curr->right) q.push(curr->right);
            total += curr->val;
        }
        res.push_back(total/n);
    }
    return res;
}
int main() {

}