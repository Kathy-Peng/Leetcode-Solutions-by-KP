# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        depth = []
        count = 1
        if not root:
            return 0
        queue = [root]
        while len(queue):
            for i in range(len(queue)):
                pop = queue.pop(0)
                if not pop.left and not pop.right:
                    depth.append(count)
                if pop.left:
                    queue.append(pop.left)
                if pop.right:
                    queue.append(pop.right)
            count += 1
            
        return min(depth)
                
                    
                    