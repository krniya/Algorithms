import collections


def maxLevelSum(root) -> int:
        queue = collections.deque([root])
        maxSum = float("-inf")
        level = maxLevel = 1
        while queue:
            currSum = 0
            for _ in range(len(queue)):
                currNode = queue.popleft()
                currSum += currNode.val
                if currNode.left:
                    queue.append(currNode.left)
                if currNode.right:
                    queue.append(currNode.right)
            if currSum > maxSum:
                maxSum = currSum
                maxLevel = level
            level+=1
        return maxLevel