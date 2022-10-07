"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        #step 1: focus on next and val first, create a copy of the original list
        dummy = ListNode(0, head)
        curr_ori = head
        copy_head = ListNode(0)
        curr_copy = copy_head
        hashmap = {}
        while curr_ori:
            #step 2: along the way, build the hashmap which maps original node to its corrresponding copy node
            new = ListNode(curr_ori.val)
            hashmap[curr_ori] = new
            curr_copy.next = new
            curr_copy = new
            curr_ori = curr_ori.next
        #step 3: go through the original list again and find where its random pointer points to, maps it to the corresponding copy pointer and update on the copy list
        curr_ori = dummy.next
        curr_copy = copy_head.next
        while curr_ori:
            random = curr_ori.random
            if not random:
                curr_copy.random = None
            else:
                copy_random = hashmap[random]
                curr_copy.random = copy_random
            curr_ori = curr_ori.next
            curr_copy = curr_copy.next
        return copy_head.next
            
        