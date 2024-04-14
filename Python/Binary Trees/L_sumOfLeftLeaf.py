class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        def f(root, isLeft):
            if not root: return 0
            if not root.left and not root.right and isLeft: return root.val
            return f(root.left, True)+f(root.right, False)
        return f(root, False)
