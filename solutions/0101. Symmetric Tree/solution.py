# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        left = root.left
        left_side = []
        left_queue = [left]
        while left_queue:
            head = left_queue.pop(0)
            if head is None:
                left_side.append(None)
                continue
            left_queue.append(head.left)
            left_queue.append(head.right)
            left_side.append(head.val)

        right = root.right
        right_side = []
        right_queue = [right]
        while right_queue:
            head = right_queue.pop(0)
            if head is None:
                right_side.append(None)
                continue
            right_queue.append(head.right)
            right_queue.append(head.left)
            right_side.append(head.val)

        return right_side == left_side