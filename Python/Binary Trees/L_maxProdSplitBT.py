def maxProduct(root) -> int:
        res = total = 0

        def dfs(root):
            if not root: return 0
            nonlocal res, total
            left, right = dfs(root.left), dfs(root.right)
            res = max(res, left * (total - left), right * (total - right))
            return left + right + root.val

        total = dfs(root)
        dfs(root)
        return res % (10**9 + 7)