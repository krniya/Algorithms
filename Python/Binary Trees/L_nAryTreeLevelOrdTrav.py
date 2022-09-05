from collections import deque


def levelOrder(root):
        if not root:
            return []
        queue = deque([root])
        res = []
        while queue:
            n = len(queue)
            child = []
            for i in range(n):
                curr = queue.popleft()
                child.append(curr.val)
                for ch in curr.children:
                    queue.append(ch)
            res.append(child)
        return res