# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
   
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        # a helper function to 
        def helper(head, k):
            curr = head
            for i in range(k):
                if curr == None:
                    return curr
                curr = curr.next
            return curr
        
        dummy_head = ListNode(0, head)
        groupPrev = dummy_head
        groupNext = None
        while True:
            #step 1: we call a helper function to move k steps forward
            kth = helper(groupPrev, k)
            if kth == None:
                break
            groupNext = kth.next
        
            #step 2: if we succeed in previous step, start reversing
            prev = groupNext
            curr = groupPrev.next
            while curr != groupNext:
                tmp = curr.next
                curr.next = prev
                prev,curr = curr, tmp
            #step 3: the dummy head we are trying to return should point to kth node
            tmp2 = groupPrev.next
            groupPrev.next = kth
            #step 4: the previous head now becomes the new group prev
            groupPrev = tmp2
            
        return dummy_head.next
        
        
        
        
        