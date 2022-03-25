def hasPathSum(root, targetSum):
    if not root:
        return
    if not root.left and not root.right and root.val == targetSum:
        return True
    targetSum -= root.val
    return hasPathSum(root.left, targetSum) or hasPathSum(root.right, targetSum)