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
        dummy_head = ListNode(0, head)
        
        left_prev, curr = dummy_head, head
        
        for i in range(left-1):
            left_prev = curr
            curr = curr.next
            
        prev = None
        for i in range(right - left + 1):
            tmpNext = curr.next
            curr.next = prev
            prev, curr = curr, tmpNext
        
        left_prev.next.next = curr
        left_prev.next = prev
        return dummy_head.next
    
            