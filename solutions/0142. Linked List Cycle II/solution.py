# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        index_mapping = {}
        idx = 0

        while head and head not in index_mapping:
            index_mapping[head] = idx
            idx += 1
            head = head.next

        if head is None:
            return None
        else:
            return head