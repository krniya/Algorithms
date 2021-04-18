# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def maxDepth(root: TreeNode) -> int:
    m = 0
    if root is None:
        return 0
    findMax(root, 0, m)
    return m


def findMax(root, s, m):
    if root is None:
        return
    s += 1
    if root.left is None and root.right is None:
        if m < s:
            m = s
    findMax(root.left, s, m)
    findMax(root.right, s, m)


c = TreeNode(15, None, None)
d = TreeNode(7, None, None)
e = TreeNode(20, c, d)
b = TreeNode(9, None, None)
a = TreeNode(3, b, e)

print(maxDepth(a))
