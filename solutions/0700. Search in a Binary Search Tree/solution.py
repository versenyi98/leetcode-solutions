# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root is None:
            return root

        if root.val == val:
            return root

        l = self.searchBST(root.left, val)
        r = self.searchBST(root.right, val)

        if l is not None:
            return l
        return r