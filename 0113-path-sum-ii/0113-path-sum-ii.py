# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return []
        results = []
        prefix_sum = 0
        result =[]
        def helper(root, prefix_sum, result):
            if not root.left and not root.right:
                prefix_sum += root.val
                if prefix_sum == targetSum:
                    result_copy = result[:]
                    result_copy.append(root.val)
                    results.append(result_copy)
            prefix_sum += root.val
            result_copy = result[:]
            result_copy.append(root.val)
            if root.left:
                helper(root.left, prefix_sum, result_copy)
            if root.right:
                helper(root.right, prefix_sum, result_copy)
        helper(root, prefix_sum, result)
        return results