# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def insertIntoBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if root==None:
            return TreeNode(val)

        if root.val > val:
            if root.left!=None:
                self.insertIntoBST(root.left,val)
            else:
                new_child = TreeNode(val)
                root.left = new_child

        #direction right:
        if root.val < val:
            if root.right !=None:
                self.insertIntoBST(root.right, val)
            else:
                new_child = TreeNode(val)
                root.right = new_child
                
        return root
        