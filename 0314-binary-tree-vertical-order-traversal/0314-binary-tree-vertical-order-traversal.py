# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getCoordinates(self, root, x, y, coordinate):
        if not root:
            return coordinate
        coordinate.append([x,y,root.val])
        coordinate = self.getCoordinates(root.left, x-1, y-1, coordinate)
        coordinate = self.getCoordinates(root.right, x+1, y-1, coordinate)
        return coordinate
        
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        coordinate = []
        #step 1: use recursion helper function to get an array of coordinates for all nodes
        coordinate = self.getCoordinates(root, 0, 0, coordinate)
        #step 2: sort the corrdinate using x, then y, then val
        coordinate.sort(key=lambda x: (x[0],-x[1]))
    
        #step 3: populate the result array
        result = [[coordinate[0][2]]]
        for i in range(1, len(coordinate)):
            if coordinate[i][0]==coordinate[i-1][0]:
                result[-1].append(coordinate[i][2])
            else:
                result.append([coordinate[i][2]])
        return result
        
        