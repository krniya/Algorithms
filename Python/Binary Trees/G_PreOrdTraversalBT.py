def preOrderTravRecursive(root, list):
    if root:
        list.append(root.data)
        preOrderTravRecursive(root.left, list)
        preOrderTravRecursive(root.right, list)


def preOrderTravIterative(root):
    if root is None:
        return
    preord = stack = []

    stack.append(root)

    while(len(stack)):
        node = stack.pop()
        preord.append(node.data)
        if node.right is not None:
            stack.append(node.right)
        if node.left is not None:
            stack.append(node.left)
    return preord
