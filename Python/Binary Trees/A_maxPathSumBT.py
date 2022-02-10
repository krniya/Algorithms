def maxPathSumBT(root):
    maxPathSum = float("-inf")
    def findMaxPath(node):
        if not node:
            return 0
        nonlocal maxPathSum
        leftMax = max(0, findMaxPath(node.left))
        rightMax = max(0, findMaxPath(node.right))
        maxPathSum = max(maxPathSum, node.val + leftMax + rightMax)
        return node.val + max(leftMax, rightMax)
    findMaxPath(root)
    return maxPathSum