def invertTree(root):
        stack = [root]
        while len(stack):
            curr = stack.pop(0)
            if curr:
                curr.left, curr.right = curr.right, curr.left
                stack += curr.left, curr.right
        return root

def invertTree2(root):
        if not root:
            return None
        tmp = root.left
        root.left = root.right
        root.right = tmp
        invertTree2(root.left)
        invertTree2(root.right)
        return root