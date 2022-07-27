def flatten(root) -> None:
    curr = root
    while curr:
        if curr.left:
            runner = curr.left
            while runner.right: runner = runner.right
            runner.right, curr.right, curr.left = curr.right, curr.left, None
        curr = curr.right