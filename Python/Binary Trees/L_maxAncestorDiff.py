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


def maxAncestorDiff(root) -> int:
    if not root:
        return 0
    diff = 0
    helper(root, root.val, root.val, diff)
    return diff

def helper(root, min_val, max_val, diff):
    if not root:
        return
    diff = max(diff, max(abs(min_val - root.val), abs(max_val - root.val)))
    min_val = min(min_val, root.val)
    max_val = max(max_val, root.val)
    helper(root.left, min_val, max_val, diff)
    helper(root.right, min_val, max_val, diff)