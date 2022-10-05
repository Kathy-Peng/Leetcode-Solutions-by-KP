# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverse(self, head):
        prev = None
        curr = head
        while curr != None:
            tmp = curr.next
            curr.next = prev
            prev, curr = curr, tmp
        return prev
        
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l1 = self.reverse(l1)
        l2 = self.reverse(l2)
        dummy_head = ListNode(0)
        curr = dummy_head
        carry = 0
        while l1 or l2:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            print(v1, v2)
            sum = v1 + v2 + carry
            carry = sum // 10
            num = sum % 10
            curr.next = ListNode(num)
            curr = curr.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        if carry != 0:
            new = ListNode(carry)
            curr.next = new
        
        return self.reverse(dummy_head.next)
            
        