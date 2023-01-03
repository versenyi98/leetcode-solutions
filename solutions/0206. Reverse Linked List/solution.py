# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, original_list):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        reversed_list = None

        while original_list:
            node = ListNode(original_list.val)
            node.next = reversed_list
            reversed_list = node
            original_list = original_list.next
        return reversed_list