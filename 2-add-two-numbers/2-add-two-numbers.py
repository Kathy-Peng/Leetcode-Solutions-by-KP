# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        curr = dummy
        carry = 0
        while l1 or l2:
            #handle edge cases when two list nodes are of different length
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            #new digit
            sum = v1 + v2 + carry
            mod = sum % 10
            carry = sum // 10
            #update variables
            curr.next = ListNode(mod)
            curr = curr.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        #handle edge case when there is a leftover carry in the begining
        if carry:
            curr.next = ListNode(carry)
        return dummy.next
            
            
            
            