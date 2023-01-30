# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ret_val = []

        if root is None:
            return ret_val

        ret_val += self.inorderTraversal(root.left)
        ret_val.append(root.val)
        ret_val += self.inorderTraversal(root.right)

        return ret_val
