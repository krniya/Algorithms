# O(n) time | O(n) space
def invertBT(tree):
    queue = [tree]
    while len(queue):
        current = queue.pop(0)
        if current is None:
            continue
        swapLeftAndRight(current)
        queue.append(current.left)
        queue.append(current.right)

# O(n) time | O(d) space
def invertBST2(tree):
    if tree is None:
        return
    swapLeftAndRight(tree)
    invertBST2(tree.left)
    invertBST2(tree.right)

def swapLeftAndRight(tree):
    tree.left, tree.right = tree.right, tree.left

