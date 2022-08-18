class Solution(object):
    def decompressRLElist(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ret_array = []
        for i in range(0,len(nums),2):
            freq = nums[i]
            value = nums[i+1]
            for j in range(freq):
                ret_array.append(value)
        return ret_array