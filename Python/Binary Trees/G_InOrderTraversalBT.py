def inOrderRecursive(root, list):
    if root:
        inOrderRecursive(root.left, list)
        list.append(root.data)
        inOrderRecursive(root.right, list)


def inOrderIterative(root):
    current = root
    inord = []
    stack = []
    while True:
        if current is not None:
            stack.append(current)
            current = current.left
        elif(len(stack)):
            current = stack.pop()
            inord.append(current.data)
            current = current.right
        else:
            return inord
