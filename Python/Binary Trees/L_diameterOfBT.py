def diameterOfBinaryTree(root) -> int:
        res = 0
        def dfs(root):
            if not root: return 0
            left = dfs(root.left)
            right = dfs(root.right)
            nonlocal res
            res = max(res, left + right)
            return 1 + max(left, right)
        dfs(root)
        return res