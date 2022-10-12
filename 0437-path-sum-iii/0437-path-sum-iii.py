# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.total_path = 0
        self.cache = {0: 1}
        
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if not root:
            return 0
        
        def helper(root, prefix_sum):
            prefix_sum += root.val
            if prefix_sum - targetSum in self.cache:
                self.total_path += self.cache[prefix_sum - targetSum]
            if prefix_sum in self.cache:
                self.cache[prefix_sum] += 1
            else:
                self.cache[prefix_sum] =1
            if root.left:
                helper(root.left, prefix_sum)
            if root.right:
                helper(root.right, prefix_sum)
            self.cache[prefix_sum]-=1
        helper(root, 0)
        return self.total_path
                
                
        
        