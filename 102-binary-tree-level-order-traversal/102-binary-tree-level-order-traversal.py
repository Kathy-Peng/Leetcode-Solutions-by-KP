# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        stack = [(1, root)]
        ret_list = []
        while len(stack)!=0:
            level, curr = stack.pop(0)
            if level > len(ret_list):
                ret_list.append([curr.val])
            else:
                curr_list = ret_list.pop()
                curr_list.append(curr.val)
                ret_list.append(curr_list)
            if curr.left:
                stack.append([level+1, curr.left])
                
            if curr.right:
                stack.append([level+1, curr.right])
        return ret_list