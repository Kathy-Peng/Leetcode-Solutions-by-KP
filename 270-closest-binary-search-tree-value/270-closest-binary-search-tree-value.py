# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def bst_search(self, root, min_diff, val, target):
        if root == None:
            return val
        if root.val == target:
            return root.val
        diff = root.val - target
        if abs(diff) < min_diff:
            min_diff = abs(diff)
            val = root.val
        if diff > 0:
            return self.bst_search(root.left, min_diff, val, target)
        if diff < 0:
            return self.bst_search(root.right, min_diff, val, target)
    
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        min_diff = 2 ** 31 - 1
        val = 0
        
        val = self.bst_search(root, min_diff, val, target)
        return val
    