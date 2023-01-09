import math


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.validate_subtree(root, -math.inf, math.inf)

    def validate_subtree(self, root, lower_bound, upper_bound):
        if root is None:
            return True

        valid = lower_bound < root.val < upper_bound
        valid = valid and self.validate_subtree(root.left, lower_bound, min(upper_bound, root.val))
        valid = valid and (root.left is None or root.val > root.left.val)
        valid = valid and self.validate_subtree(root.right, max(lower_bound, root.val), upper_bound)
        valid = valid and (root.left is None or root.val > root.left.val)

        return valid