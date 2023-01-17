# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ret_val = []

        if root is None:
            return ret_val

        ret_val += self.postorderTraversal(root.left)
        ret_val += self.postorderTraversal(root.right)
        ret_val.append(root.val)

        return ret_val