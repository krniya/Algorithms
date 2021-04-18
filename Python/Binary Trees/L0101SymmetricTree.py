# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root is None:
            return True
        return self.symmetricHelper(root.left, root.right)

    def symmetricHelper(self, left, right):
        if not left and not right:
            return True
        if not left or not right:
            return False
        if left.val == right.val:
            out = self.symmetricHelper(left.left, right.right)
            inn = self.symmetricHelper(left.right, right.left)
            return out and inn
        else:
            return False

    def isSymmetric(self, root: TreeNode) -> bool:
        if root is None:
            return True
        stack = [[root.left, root.right]]
        while len(stack) > 0:
            pair = stack.pop(0)
            left = pair[0]
            right = pair[1]
            if left is None and right is None:
                continue
            if left is None or right is None:
                return False
            if left.val == right.val:
                stack.insert(0, [left.left, right.right])
                stack.insert(0, [left.right, right.left])
            else:
                return False
        return True
