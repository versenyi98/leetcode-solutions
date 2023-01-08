# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []

        queue = [(root, 0)]
        ret_val = []

        while queue:
            head, level = queue.pop(0)
            if level == len(ret_val):
                ret_val.append([])
            ret_val[level].append(head.val)

            if head.left is not None:
                queue.append((head.left, level + 1))
            if head.right is not None:
                queue.append((head.right, level + 1))
        return ret_val