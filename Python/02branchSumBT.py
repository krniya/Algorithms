class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None

# O(n) Time | O(n) Space
def branchSums(root):
    sums = []
    calBranchSums(root, 0, sums)
    return sums


def calBranchSums(node, runningSum, sums):
    if node is None:
        return
    
    newRunningSum = runningSum + node.value
    if node.left is None and node.right is None:
        sums.append(newRunningSum)
        return
    
    calBranchSums(node.left, newRunningSum, sums)
    calBranchSums(node.right, newRunningSum, sums)