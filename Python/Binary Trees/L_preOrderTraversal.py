from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def preorderTraversal(root: Optional[TreeNode]) -> List[int]:
        res = []
        def traverse(root):
            if not root: return
            res.append(root.val)
            traverse(root.left)
            traverse(root.right)
        traverse(root)
        return res