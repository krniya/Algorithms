from functools import total_ordering


class Solution:
    def convertBST(self, root):
        total = 0
        def helper(root):
            nonlocal total
            if not root: return
            helper(root.right)
            total += root.val
            root.val = total
            helper(root.left)
            return root
        return helper(root)