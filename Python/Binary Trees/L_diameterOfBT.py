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
    
def diameterOfBinaryTree1(root) -> int:
        diameter = [0]
        def helper(node):
            if not node:
                return 0
            left = helper(node.left)
            right = helper(node.right)
            diameter[0] = max(diameter[0], left + right)
            return max(left, right) + 1
        helper(root)
        return diameter[0]