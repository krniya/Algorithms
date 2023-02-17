from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def minDiffInBST(root: Optional[TreeNode]) -> int:
        def inorder(node, pre, rst):
            if not node: return
            inorder(node.left, pre, rst)
            pre[0], rst[0] = node.val, min(rst[0], node.val - pre[0])
            inorder(node.right, pre, rst)
            
        pre, rst = [-float('inf')], [float('inf')]
        inorder(root, pre, rst)
        #BST size >= 2, solid result guaranted.
        return rst[0]