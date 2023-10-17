from collections import deque
from typing import List


def validateBinaryTreeNodes(n: int, leftChild: List[int], rightChild: List[int]) -> bool:
    root = 0
    childrenNodes = set(leftChild + rightChild)
    for i in range(n):
        if i not in childrenNodes:
            root = i
    visited = set()
    queue = deque([root])

    while queue:
        node = queue.popleft()
        if node in visited:
            return False
        visited.add(node)
        if leftChild[node] != -1:
            queue.append(leftChild[node])
        if rightChild[node] != -1:
            queue.append(rightChild[node])
    return len(visited) == n