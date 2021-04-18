def isBST(root):
    return isBSTUtil(root, float("-inf"), float("inf"))


def isBSTUtil(node, mini, maxi):
    if node is None:
        return True
    if node.data < mini or node.data > maxi:
        return False
    return (isBSTUtil(node.left, mini, node.data - 1) and
            isBSTUtil(node.right, node.data+1, maxi))
