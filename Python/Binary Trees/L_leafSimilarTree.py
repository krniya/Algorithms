def leafSimilar(root1, root2) -> bool:
    def dfs(root):
        if not root:
            return []
        if not root.left and not root.right:
            return [root.val]
        return dfs(root.left) + dfs(root.right)
    return dfs(root1) == dfs(root2)


def leafSimilar1(root1, root2) -> bool:
    def get_leaves(root):
        leaves  = []
        stack = [root]
        while stack:
            node = stack.pop()
            if not node.left and not node.right:
                leaves.append(node.val)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return leaves
    return get_leaves(root1) == get_leaves(root2)