# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        looking_for = set()

        queue = [root]

        while queue:
            head = queue.pop(0)

            if head is None:
                continue

            if head.val in looking_for:
                return True

            looking_for.add(k - head.val)
            queue.append(head.left)
            queue.append(head.right)
        return False
