def leftViewUtil(result, node, level):
    global max_level
    if (node == None):
        return

    if (max_level < level):
        result.append(node.data)
        max_level = level

    leftViewUtil(result, node.left, level+1)
    leftViewUtil(result, node.right, level+1)


def LeftView(root):
    '''
    :param root: root of given tree.
    :return: print the left view of tree, dont print new line
    '''
    global max_level
    max_level = 0
    result = []
    leftViewUtil(result, root, 1)
    return result
