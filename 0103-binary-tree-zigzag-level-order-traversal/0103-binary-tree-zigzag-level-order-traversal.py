# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue = [root]
        result = []
        order = True
        while len(queue):
            if not order:
                level = [queue[i].val for i in range(len(queue)-1, -1, -1)]
                order = True
            else:
                level = [node.val for node in queue]
                order = False
                
            result.append(level)
            for i in range(len(queue)):
                popped = queue.pop(0)
                if popped.left:
                    queue.append(popped.left)
                if popped.right:
                    queue.append(popped.right)
        return result
            
                        