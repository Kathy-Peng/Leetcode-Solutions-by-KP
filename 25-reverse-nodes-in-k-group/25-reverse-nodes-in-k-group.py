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
        def helper(head, k):
            curr = head
            for i in range(k):
                if curr == None:
                    return curr
                curr = curr.next
            return curr
        
        #step 1: we call a helper function to move k steps forward
        dummy_head = ListNode(0, head)
        groupPrev = dummy_head
        groupNext = None
        while True:
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
            
            tmp2 = groupPrev.next
            groupPrev.next = kth
            groupPrev = tmp2
        
        #step 3: move on to the start node of the next k group and repeat the process
        
        #step 4: connect the last node of previous k group to the start of next k group
        return dummy_head.next
        
        
        
        
        