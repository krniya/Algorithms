class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def inorderMorris(root):
    cur = root
    while cur:
        if cur.left:
            temp = cur.left                                                      
            while temp.right and temp.right != cur:
                temp = temp.right                
            if not temp.right:                                             
                temp.right, cur = cur, cur.left   
                continue                                   
            temp.right = None                      
        print(cur.val, end=" ")
        cur = cur.right

one = TreeNode(1)
two = TreeNode(2)
three = TreeNode(3)
four = TreeNode(4)
five = TreeNode(5)
six = TreeNode(6)

one.left = two
one.right = three

two.left = four
two.right = five

five.right = six

inorderMorris(one)
