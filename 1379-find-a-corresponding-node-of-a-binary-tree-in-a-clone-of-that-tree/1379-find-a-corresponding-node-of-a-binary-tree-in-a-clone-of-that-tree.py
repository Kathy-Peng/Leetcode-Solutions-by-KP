# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        val = target.val
        queue = [cloned]
        while len(queue):
            pop = queue.pop(0)
            if pop.val == val:
                return pop
            if pop.left:
                queue.append(pop.left)
            if pop.right:
                queue.append(pop.right)
        