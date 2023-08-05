from typing import List, Optional


class TreeNode:
    """TreeNode class""" 
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def generate_tree(number_of_nodes: int) -> List[Optional[TreeNode]]:
    """_summary_
        Generate all the possible BST in range of 1 to number_of_nodes
    Args:
        number_of_nodes (int): _description_

    Returns:
        List[Optional[TreeNode]]: _description_
    """
    cache = {}
    def generate(left, right):
        if (left, right) in cache:
            return cache[(left, right)]
        if left == right:
            return [TreeNode(left)]
        if left > right:
            return [None]
        result = []
        for root_value in range(left, right+1):
            for left_node in generate(left, root_value - 1):
                for right_node in generate(root_value + 1, right):
                    root = TreeNode(root_value, left_node, right_node)
                    result.append(root)
        cache[(left, right)] = result
        return result
    return generate(1, number_of_nodes)