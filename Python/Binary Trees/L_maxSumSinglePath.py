def maxPathSum(root) -> int:
        res = root.val
        def dfs(root):
            if not root:
                return 0
            leftmax = max(0, dfs(root.left))
            rightmax = max(0, dfs(root.right))
            nonlocal res
            res = max(res, root.val + leftmax + rightmax)
            return root.val + max(leftmax, rightmax)
        dfs(root)
        return res