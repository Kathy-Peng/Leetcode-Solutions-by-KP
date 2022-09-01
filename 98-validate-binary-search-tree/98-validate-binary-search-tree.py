# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        #use in-order traversal and verify that it's sorted
        in_order_list = []
        
        def recur(root, in_order_list):
            if root.left:
                recur(root.left, in_order_list)
            in_order_list.append(root.val)
            if root.right:
                recur(root.right, in_order_list)
        recur(root, in_order_list)  
        print(in_order_list)
        #verify that in order list is sorted
        flag = True
        for i in range(1, len(in_order_list)):
            if in_order_list[i]<=in_order_list[i-1]:
                flag = False
        return flag
            
        
        
            