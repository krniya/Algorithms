class Node:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None


def insert(root, node):
    if root is None:
        root = node
    else:
        if root.value < node.value:
            if root.right is None:
                root.right = node
            else:
                insert(root.right, node)
        else:
            if root.left is None:
                root.left = node
            else:
                insert(root.left, node)


def inorder(root):
    if root:
        inorder(root.left)
        print(root.value)
        inorder(root.right)


# Average O(log(n)) | O(log(n))
# Worst   O(n)      | O(n)
def closestValueBST(tree, tar):
    return closestValueBSTHelper(tree, tar, float("inf"))


def closestValueBSTHelper(tree, tar, closest):
    if tree is None:
        return closest
    if abs(tar - closest) > abs(tar - tree.value):
        closest = tree.value
    if tar < tree.value:
        return closestValueBSTHelper(tree.left, tar, closest)
    elif tar > tree.value:
        return closestValueBSTHelper(tree.right, tar, closest)
    else:
        return closest

# Average O(log(n)) | O(1)
# Worst   O(n)      | O(1)


def closestValueBST1(tree, tar):
    return closestValueBSTHelper1(tree, tar, float("inf"))


def closestValueBSTHelper1(tree, tar, closest):
    currentNode = tree
    while currentNode is not None:
        if abs(tar - closest) > abs(tar - currentNode.value):
            closest = currentNode.value
        if tar < currentNode.value:
            currentNode = currentNode.left
        elif tar > currentNode.value:
            currentNode = currentNode.right
        else:
            break
    return closest


r = Node(50)
insert(r, Node(30))
insert(r, Node(20))
insert(r, Node(40))
insert(r, Node(70))
insert(r, Node(60))
insert(r, Node(80))

inorder(r)
print(closestValueBST1(r, 32))
