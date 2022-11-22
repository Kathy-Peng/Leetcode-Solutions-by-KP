# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy1 = head
        dummy2 = head
        while dummy2.next and dummy2.next.next:
            dummy2 = dummy2.next.next
            dummy1 = dummy1.next
        return dummy1.next if dummy2.next else dummy1