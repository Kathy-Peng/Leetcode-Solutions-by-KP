"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return
        dummy = root
        queue = [root]
        while len(queue):
            for i in range(len(queue)-1):
                queue[i].next = queue[i+1]
            queue[-1].next = None
            for j in range(len(queue)):
                popped = queue.pop(0)
                if popped.left:
                    queue.append(popped.left)
                if popped.right:
                    queue.append(popped.right)
        return dummy