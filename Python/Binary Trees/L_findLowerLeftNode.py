from collections import deque


def findBottomLeftValue(root) -> int:
    bottom_left = 0
    queue = deque([root])
    while queue:
        bottom_left = queue[0].val
        for _ in range(len(queue)):
            curr_node = queue.popleft()
            if curr_node.left:
                queue.append(curr_node.left)
            if curr_node.right:
                queue.append(curr_node.right)
    return bottom_left