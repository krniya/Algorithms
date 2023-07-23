class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def allPossibleFBT(n: int):
        if n%2==0 or n<1:
            return []

        dp=[[] for _ in range(n+1)]
        dp[1]=[TreeNode(0)]

        for i in range(3,n+1):
            for j in range(1,i):
                leftTree=dp[j]
                rightTree=dp[i-1-j]

                for leftSubtree in leftTree:
                    for rightSubtree in rightTree:
                        root=TreeNode(0)
                        root.left=leftSubtree
                        root.right=rightSubtree
                        dp[i].append(root)

        return dp[n]             