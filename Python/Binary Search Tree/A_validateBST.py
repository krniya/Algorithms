# O(n) | O(d)
def validateBST(root):
    return validateBSTHelper(root, float("-inf"), float("inf"))

def validateBSTHelper(node, min, max):
    if node is None:
        return True
    if node.value < min or node.value >= max:
        return False
    leftIsValid = validateBSTHelper(node.left, min, node.value)
    return leftIsValid and validateBSTHelper(node.right, node.value, max)

