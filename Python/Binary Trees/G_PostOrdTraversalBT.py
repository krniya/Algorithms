def postOrdTravRecursive(root, list):
    if root:
        postOrdTravRecursive(root.left, list)
        postOrdTravRecursive(root.right, list)
        list.append(root.data)


ans = []


def postOrdTravIterative(root):
    if root is None:
        return
    stack = []
    while(True):
        while (root):
            if root.right is not None:
                stack.append(root.right)
            stack.append(root)
            root = root.left
        root = stack.pop()
        if (root.right is not None and peek(stack) == root.right):
            stack.pop()
            stack.append(root)
            root = root.right
        else:
            ans.append(root.data)
            root = None
        if (len(stack) <= 0):
            break
