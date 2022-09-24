def pathSum(root, targetSum: int):
        def dfs(root, targetSum, path):
            if not root:
                return None
            targetSum -= root.val
            path.append(root.val)
            if not root.left and not root.right and targetSum == 0:
                ans.append(path.copy())
            dfs(root.left, targetSum, path)
            dfs(root.right, targetSum, path)
            path.pop()
        ans = []
        dfs(root, targetSum, [])
        return ans