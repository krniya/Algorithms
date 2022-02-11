from collections import deque


def BTLevelOrderTraversal(root):
    if not root:
        return []
    res, queue = [], deque([root])
    while queue:
        curr, size = [], len(queue)
        for i in range(size):
            node = queue.pop()
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            curr.append(node.value)
        res.append(curr)
    return res