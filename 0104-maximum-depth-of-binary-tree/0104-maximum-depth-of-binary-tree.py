# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        queue = [root]
        depth = 0
        while len(queue):
            for i in range(len(queue)):
                pop = queue.pop(0)
                if pop.left:
                    queue.append(pop.left)
                if pop.right:
                    queue.append(pop.right)
            depth += 1
        return depth
            
                
            