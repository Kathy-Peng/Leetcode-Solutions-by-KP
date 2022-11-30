# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        return self.bfs(root , float('-inf') , float('inf'))

    def bfs(self , root , left  , right):
        if root==None:
            return True

        if not left < root.val <right:
            return False
        
        return self.bfs(root.left , left , root.val) and self.bfs(root.right , root.val , right)

            
        
        
            