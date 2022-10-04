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
            #given head, moves head k steps forward
            for i in range(k):
                if head == None:
                    return None
                head = head.next
            return head
        
        dummy_head = ListNode(0, head)
        groupPrev = dummy_head
        curr = head
        while True:
            kth = helper(groupPrev, k) 
            if not kth:
                break
            #we need a new variable to reference this node after kth
            #otherwise if we later modify where kth is pointing to this kth.next 
            #will also be changed into something else
            groupNext = kth.next
            prev = groupNext
            while curr!=groupNext:
                tmp = curr.next
                curr.next = prev
                prev, curr = curr, tmp
            #update where current groupPrev is pointing and update what groupPrev should be next
            newgroupprev = groupPrev.next 
            groupPrev.next = kth
            groupPrev = newgroupprev
            
        return dummy_head.next
        
        
        
        
        