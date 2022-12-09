def maxAncestorDiff(root) -> int:
        ans = 0
        def dfs(root):
            if not root: return float("inf"), float("-inf")
            leftMin, leftMax = dfs(root.left)
            rightMin, rightMax = dfs(root.right)
            curMin, curMax = min(root.val, leftMin, rightMin), max(root.val, leftMax, rightMax)
            ans = max(ans, root.val - curMin, curMax - root.val)
            return curMin, curMax
        dfs(root)
        return ans