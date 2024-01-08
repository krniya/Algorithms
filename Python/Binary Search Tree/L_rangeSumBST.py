from collections import deque


def rangeSumBST(root, low: int, high: int) -> int:
        res = 0
        def preOrd(root):
            if not root:
                return
            preOrd(root.left)
            nonlocal res
            if low <= root.val <= high:
                res += root.val
            preOrd(root.right)
        preOrd(root)
        return res
    
    
def rangeSumBST1(root, lo: int, hi: int) -> int:
    res = 0
    q = deque([root])
    while q:
        c = q.popleft()
        v, l, r = c.val, c.left, c.right
        if lo <= v and v <= hi:
            res += v
        if l and (lo < v or v > hi):
            q.append(l)
        if r and (lo > v or v < hi):
            q.append(r)
    return res