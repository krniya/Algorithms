def getDirections(root, startValue: int, destValue: int):
    path = []
    def find(node, curr, val):
        if not node:
            return
        if node.val == val:
            path.append(curr.copy())
            return
        if node.left:
            curr.append("L")
            find(node.left, curr, val)
            curr.pop()
        if node.right:
            curr.append("R")
            find(node.right, curr, val)
            curr.pop()
    find(root, [], startValue)
    find(root, [], destValue)
    res = ""
    start, end = path
    while(start and end and start[0] == end[0]):
        start.pop(0)
        end.pop(0)
    for _ in start:
        res+= "U"
    for ch in end:
        res += ch
    return res
        
        
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
a = TreeNode(1)
ar = TreeNode(10)
arl = TreeNode(12)
arlr = TreeNode(6)
arr = TreeNode(13)
arrr = TreeNode(15)
a.right = ar
ar.left = arl
arl.right = arlr
ar.right = arr
arr.right = arrr

print(getDirections(a, 6, 15))