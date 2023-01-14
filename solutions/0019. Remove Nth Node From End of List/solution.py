# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        node = head

        while node:
            length += 1
            node = node.next

        skip_next = length - n
        if skip_next < 0:
            return head
        if skip_next == 0:
            return head.next

        idx = 0
        node = head
        while node:
            idx += 1
            if idx == skip_next:
                node.next = node.next.next if node.next else None
            else:
                node = node.next

        return head