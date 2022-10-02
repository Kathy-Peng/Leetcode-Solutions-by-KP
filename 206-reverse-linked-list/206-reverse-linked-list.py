# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        #two pointer method: prev, curr
        #as we traverse the linked list, we make curr points to prev
        #and then iterate the process until we hit the end of curr, return curr
        
        #step1: initialize two pointers prev and curr
        prev = None
        curr = head
        #step 2: go into for loop and make curr points to prev
        while curr:
            #store a tmp for next node
            tmp = curr.next
            #actual reversing step
            curr.next = prev
            #update both curr and prev
            prev = curr
            curr = tmp
        #step 3: make dummy head points to curr and return as result
        return prev
            
            