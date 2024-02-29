from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isEvenOddTree(root) -> bool:
    odd_inc = True
    queue = deque([root])
    while queue:
        prev = float("-inf") if odd_inc else float("inf")
        for _ in range(len(queue)):
            curr_node = queue.popleft()
            if odd_inc and (prev >= curr_node.val or curr_node.val % 2 == 0):
                return False
            if not odd_inc and (prev <= curr_node.val or curr_node.val % 2== 1):
                return False
            if curr_node.left:
                queue.append(curr_node.left)
            if curr_node.right:
                queue.append(curr_node.right)
            prev = curr_node.val
        odd_inc = not odd_inc
    return True

# def build_tree(nodes, index):
#     if index < len(nodes) and nodes[index] is not None:
#         node = TreeNode(nodes[index])
#         node.left = build_tree(nodes, 2 * index + 1)
#         node.right = build_tree(nodes, 2 * index + 2)
#         return node
#     return None

# def deserialize(data):
#     nodes = data.split(',')
#     for i in range(len(nodes)):
#         if nodes[i] == 'null':
#             nodes[i] = None
#         else:
#             nodes[i] = int(nodes[i])
#     return build_tree(nodes, 0)

# # Example usage:
# data = [1, 10, 4, 3, None, 7, 9, 12, 8, 6, None, None, 2]
# # data = [5,4,2,3,3,7]
# serialized_data = ','.join(str(val) if val is not None else 'null' for val in data)
# root = deserialize(serialized_data)

# print(isEvenOddTree(root))
