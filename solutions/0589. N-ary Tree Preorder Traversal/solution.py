"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        ret_val = []
        if root is None:
            return ret_val

        ret_val = [root.val]

        for child in root.children:
            ret_val += self.preorder(child)
        return ret_val