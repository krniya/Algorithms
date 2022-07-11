def rightSideView(root):
        res = []
        def traverse(node, depth):
            if not node:
                return None
            if len(res) <= depth:
                res.append(node.val)
            traverse(node.right, depth + 1)
            traverse(node.left,  depth + 1)
        
        traverse(root, 0)
        return res