def evaluateTree(root) -> bool:
        if root.val == 0:
            return False
        elif root.val == 1:
            return True
        elif root.val == 2:
            return evaluateTree(root.left) or evaluateTree(root.right)
        elif root.val == 3:
            return evaluateTree(root.left) and evaluateTree(root.right)