def longestZigZag(root) -> int:
        maxLength = 0
        def solve(node, deep, dir):
            nonlocal maxLength
            maxLength = max(maxLength, deep)

            if node.left is not None:
                solve(node.left, deep+1,'left') if dir != 'left' else solve(node.left, 1, 'left')
            if node.right is not None:
                solve(node.right, deep+1, 'right') if dir != 'right' else solve(node.right, 1, 'right')
        solve(root, 0, '')
        return maxLength