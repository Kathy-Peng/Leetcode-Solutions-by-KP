# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        if not head.next:
            return head
        prev = self.reverseList(head.next)
        #we make head.next points to head itself, reversing the direction
        head.next.next = head
        head.next = None
        return prev