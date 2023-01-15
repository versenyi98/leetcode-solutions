# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head, val):
        new_head = None
        while new_head is None and head:
            if head.val != val:
                new_head = head
            head = head.next
        new_tail = new_head

        while head:
            if head.val != val:
                new_tail.next = head
                new_tail = new_tail.next
            head = head.next

        if new_tail:
            new_tail.next = None

        return new_head