from collections import deque


def averageOfLevels(root):
        queue = deque([root])
        res = []
        while queue:
            n = len(queue)
            total = 0
            for i in range(n):
                curr = queue.popleft()
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
                total += curr.val
            res.append(total/n)
        return res