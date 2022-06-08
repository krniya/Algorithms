import collections


def maxDepth(root) -> int:
        if not root:
            return 0
        height = 0
        q = collections.deque([root])
        while q:
            s = len(q)
            for i in range(s):
                curr = q.popleft()
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
            height += 1
        return height


def maxDepth(root):
        def dfs(root,depth):
            if root is None:
                return depth
            return max(dfs(root.left, depth + 1), dfs(root.right, depth + 1))
        return dfs(root,0)