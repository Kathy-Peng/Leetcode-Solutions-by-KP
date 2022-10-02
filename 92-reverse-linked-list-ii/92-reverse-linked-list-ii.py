# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: ListNode
        :type left: int
        :type right: int
        :rtype: ListNode
        """
        # step 1: move to the left index using two pointers
        dummy = ListNode(0, head)
        groupPrev = dummy
        curr = head
        for i in range(left - 1):
            groupPrev = curr
            curr = curr.next
        # step 2: start reversing nodes from left index and stop at right index
        prev = None
        for j in range(right - left + 1):
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        # step 3: make groupPrev point to right and make left point to groupNext
        groupPrev.next.next = curr
        groupPrev.next = prev
        return dummy.next
        
    
            