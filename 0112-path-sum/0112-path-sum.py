# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        target = []
        prefix_sum = 0
        def helper(root, prefix_sum):
            if not root.left and not root.right:
                prefix_sum += root.val
                if prefix_sum == targetSum:
                    target.append(prefix_sum)
            prefix_sum += root.val
            if root.left:
                helper(root.left, prefix_sum)
            if root.right:
                helper(root.right, prefix_sum)
        helper(root, prefix_sum)
        return len(target)!=0