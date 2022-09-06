def pruneTree(root):
        def dfs(root):
            if not root:
                return 0
            left = dfs(root.left)
            if not left:
                root.left = None
            right = dfs(root.right)
            if not right:
                root.right = None
            return left or right or root.val
        dfs(root)
        return root if root.left or root.right or root.val else None