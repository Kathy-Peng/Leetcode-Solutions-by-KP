# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
#class ArrayReader(object):
#    def get(self, index):
#        """
#        :type index: int
#        :rtype int
#        """

class Solution(object):
    def search(self, reader, target):
        """
        :type reader: ArrayReader
        :type target: int
        :rtype: int
        """
        l = 0
        r = 10000
        #find exact index of the target
        while l <= r:
            mid = (l + r) /2
            num = reader.get(mid)
            print(mid, num)
            if num == 2**31 -1:
                r = mid - 1
            else:
                if num == target:
                    return mid
                if num > target:
                    r = mid -1
                if num < target:
                    l = mid + 1
        return -1