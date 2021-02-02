def printAllDups(root):
    m = {}
    return inorder(root, m)


def inorder(node, m):
    if (not node):
        return ""

    Str = "("
    Str += inorder(node.left, m)
    Str += str(node.data)
    Str += inorder(node.right, m)
    Str += ")"

    if (Str in m and m[Str] == 1):
        print(node.data, end=" ")
    if Str in m:
        m[Str] += 1
    else:
        m[Str] = 1
    return Str
