# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        head = None
        tail = None

        while list1 is not None or list2 is not None:
            if list1 is None:
                next_value = list2.val
                list2 = list2.next
            elif list2 is None:
                next_value = list1.val
                list1 = list1.next
            elif list1.val > list2.val:
                next_value = list2.val
                list2 = list2.next
            else:
                next_value = list1.val
                list1 = list1.next

            if head is None:
                head = ListNode(next_value)
                tail = head
            else:
                tail.next = ListNode(next_value)
                tail = tail.next
        return head