from collections import deque


def minDepth(root) -> int:
        if not root:
            return 0
        queue = deque([root])
        minLength = 1
        while queue:
            for _ in range(len(queue)):
                currentNode = queue.popleft()
                if not currentNode.left and not currentNode.right:
                    return minLength
                if currentNode.left:
                    queue.append(currentNode.left)
                if currentNode.right:
                    queue.append(currentNode.right)
            minLength += 1
            