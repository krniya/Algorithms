def kthSmallest(root, k):
        stack = []
        curr = root
        while stack or curr:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            k -= 1
            if k == 0:
                return curr.val
            curr = curr.right


def kthSmallest(root, k):
        res = 0
        def inOrd(root):
            nonlocal res, k
            if not root: return
            inOrd(root.left)
            k-=1
            if k == 0:
                res = root.val
                return
            inOrd(root.right)
        inOrd(root)
        return res