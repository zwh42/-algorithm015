"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if not root:
            return []

        result = []
        node_list = [root]
        while node_list:
            current_node = node_list.pop()
            result.append(current_node.val)
            if current_node.children is not None:
                for child in current_node.children[::-1]:
                    node_list.append(child)



        return result