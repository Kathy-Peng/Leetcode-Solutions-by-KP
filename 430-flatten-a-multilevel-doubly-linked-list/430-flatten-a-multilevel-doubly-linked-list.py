"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution(object):
    def flatten(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        #recursion: takes in the first node of the level as input
        #returns a linked list containing the flattened list
        dummy_head = ListNode(0, head)
        
        def recursion(head):
            while head:
                tmp = head.next
                if head.child:
                    tail = recursion(head.child)
                    head.next = head.child
                    head.child.prev = head
                    head.child = None
                    #edge case: the head is already the last node and it has a child
                    if not tmp:
                        return tail
                    tail.next = tmp
                    tmp.prev = tail
                if tmp == None:
                    return head
                head = tmp
        recursion(dummy_head.next)
        return dummy_head.next
            