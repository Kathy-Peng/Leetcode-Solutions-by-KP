# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
#class ArrayReader(object):
#	 # Compares the sum of arr[l..r] with the sum of arr[x..y]
#	 # return 1 if sum(arr[l..r]) > sum(arr[x..y])
#	 # return 0 if sum(arr[l..r]) == sum(arr[x..y])
#	 # return -1 if sum(arr[l..r]) < sum(arr[x..y])
#    def compareSub(self, l, r, x, y):
#        """
#        :type l, r, x, y: int
#        :rtype int
#        """
#
#	 # Returns the length of the array
#    def length(self):
#        """
#        :rtype int
#        """

class Solution(object):
    def getIndex(self, reader):
        """
        :type reader: ArrayReader
        :rtype: integer
        """
        
        l = 0
        y = reader.length()-1
        while l < y - 1:
            mid = (l + y) /2
            ans = reader.compareSub(l, mid, y+l-mid, y)
            if ans == 1:
                y = mid
            elif ans == -1:
                l = mid + 1
            else:
                return (l+y)/2
        if reader.compareSub(l,l, y,y)==1:
            return l
        else:
            return y
        