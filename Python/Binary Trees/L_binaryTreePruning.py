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


def pruneTree(root):
        if not root: return None
        root.left = pruneTree(root.left)
        root.right = pruneTree(root.right)
        if not root.left and not root.right and not root.val: return None
        return root