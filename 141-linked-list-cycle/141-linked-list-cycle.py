# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        fp = head
        sp = head
        if not head:
            return False
        if head.next:
            if head.next.next:
                fp = head.next.next
            sp = head.next
        else:
            #if there is one node then no cycle
            return False
        while fp!= sp:
            if sp.next==None:
                return False
            if fp.next == None or fp.next.next == None:
                return False
            fp = fp.next.next 
            sp = sp.next
        return True
        