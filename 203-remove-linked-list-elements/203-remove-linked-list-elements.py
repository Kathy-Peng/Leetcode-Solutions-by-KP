# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        #find the first node that doesn't needs removal
        dummy_head = ListNode()
        dummy_head.next = head
        curr = dummy_head
        #while curr still points to something
        while curr.next:
            if curr.next.val == val:
                # if the next node is to be deleted
                # we connect node with the next node's next node
                # and we do not upate curr itself so we will check curr.next again
                curr.next = curr.next.next
            else:
                #only move curr one step forward if the next node is to stay
                curr = curr.next
        return dummy_head.next
        