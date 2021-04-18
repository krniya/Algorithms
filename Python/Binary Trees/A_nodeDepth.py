# O(n) | O(h)
def nodeDepth(tree, depth = 0):
    if tree is None:
        return 0
    return depth + nodeDepth(tree.left, depth + 1) + nodeDepth(tree.right, depth + 1)

# O(n) | O(h)
def nodeDepth1(tree):
    sumOfDepth = 0
    stack = [{"node" : tree, "depth" : 0}]
    while len(stack) > 0:
        nodeInfo = stack.pop()
        node, depth = nodeInfo["node"], nodeInfo["depth"]
        if node is None:
            continue
        sumOfDepth += depth
        stack.append({"node" : node.left, "depth": depth + 1})
        stack.append({"node" : node.right, "depth": depth + 1})
    return sumOfDepth
