from collections import deque

def connect(root):
    if not root:
        return None
    q = deque([root])
    while q:
        rightNode = None
        for _ in range(len(q)):
            cur = q.popleft()
            cur.next, rightNode = rightNode, cur
            if cur.right:
                q.extend([cur.right, cur.left])
    return root