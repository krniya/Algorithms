def minValue(root):
    if root.left is None:
        return root.data
    while root.left is not None:
        root = root.left
    return root.data


def maxValue(root):
    if root.right is None:
        return root.data
    while root.right is not None:
        root = root.right
    return root.data
