# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, row, col):
#        """
#        :type row : int, col : int
#        :rtype int
#        """
#
#    def dimensions:
#        """
#        :rtype list[]
#        """

class Solution(object):
    def leftMostColumnWithOne(self, binaryMatrix):
        """
        :type binaryMatrix: BinaryMatrix
        :rtype: int
        """
        dim = binaryMatrix.dimensions()
        row, col = dim[0], dim[1]
        minCol = col
        for i in range(row):
            l = 0
            r = col - 1
            #find first occurance of 1
            while l < r:
                mid = (l + r ) / 2
                if binaryMatrix.get(i, mid)==1:
                    r = mid 
                else:
                    l = mid + 1
            if binaryMatrix.get(i, l)==1 and l < minCol:
                minCol = l
        return minCol if minCol != col else -1
                
        