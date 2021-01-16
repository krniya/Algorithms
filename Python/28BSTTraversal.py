def inOrder(tree, inord):
    if tree is not None:
        inOrder(tree.left, inord)
        inord.append(tree.value)
        inOrder(tree.right, inord)
    return inord

def preOrder(tree, preord):
    if tree is not None:
        preord.append(tree.value)
        preOrder(tree.left, preord)
        preOrder(tree.right, preord)
    return preord

def postOrder(tree, postord):
    if tree is not None:
        postOrder(tree.left, postord)
        postOrder(tree.right, postord)
        postord.append(tree.value)
    return postord