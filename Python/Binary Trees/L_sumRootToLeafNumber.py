def sumNumbers(root) -> int:
        def dfs(root, sum):
            if not root:
                return 0
            sum = sum * 10 + root.val
            if not root.left and not root.right:
                return sum
            return dfs(root.left, sum) + dfs(root.right, sum)
        return dfs(root, 0)