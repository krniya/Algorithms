def distributeCoins(root) -> int:
    #move coins to parent DFS
    def f(root, parent):
        if root==None: return 0
        moves=f(root.left, root)+f(root.right, root)
        x=root.val-1
        if parent!=None: parent.val+=x
        moves+=abs(x)
        return moves
    return f(root, None)