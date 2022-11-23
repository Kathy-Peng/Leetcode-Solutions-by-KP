# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from heapq import heapify, heappush, heappop
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        heapify(heap)
        dummy_head = ListNode()
        curr = ListNode()
        dummy_head.next = curr
        for i, lst in enumerate(lists):
            if lst:
                heappush(heap, (lst.val, i))
        while len(heap):
            val, idx = heappop(heap)
            #using idx to get item and add it to result
            item = lists[idx] 
            curr.next = item 
            curr = curr.next
            if item.next:
                lists[idx]=item.next
                heappush(heap,(item.next.val, idx))
        return dummy_head.next.next
            
        