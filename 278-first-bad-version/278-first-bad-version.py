# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):
class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left_index = 1
        right_index = n
        median = n // 2 + 1
        while left_index != right_index:
            if isBadVersion(median) == True:
                right_index = median
                median = (left_index + median)//2
            else:
                left_index = median+1
                median = (right_index + median) // 2
        return right_index
        