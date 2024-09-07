def isSubPath(head, root):
        return dfs(head, head, root)

def dfs(head, cur, root):
    if cur is None:  # Successfully matched the list
        return True
    if root is None:  # Reached the end of the tree without matching
        return False
    
    if cur.val == root.val:
        cur = cur.next  # Move to the next list node if value matches
    elif head.val == root.val:
        head = head.next  # Start new matching attempt if the value matches head of list
    else:
        cur = head  # Reset the matching pointer

    # Recursively check left and right subtrees
    return dfs(head, cur, root.left) or dfs(head, cur, root.right)