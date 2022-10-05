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
        dummy_head = ListNode(0)
        curr = dummy_head
        carry = 0
        #step 1: loop until we hit the end of both list
        while l1 or l2:
            #step 2: extract values from both lists and add them up alongside carry
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            print(v1, v2)
            sum = v1 + v2 + carry
            #step 3: calculate the floor division and modulo of the sum 
            #and create new node to reflect this and update carry
            carry = sum // 10
            num = sum % 10
            curr.next = ListNode(num)
            curr = curr.next 
            #step 4: move on to the next nodes in the list
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        #step 5: if there is a carry term make sure to include it
        print(carry)
        if carry != 0:
            new = ListNode(carry)
            curr.next = new
        return dummy_head.next
            
            
            