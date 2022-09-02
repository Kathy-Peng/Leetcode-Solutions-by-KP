class Solution(object):
    def countPairs(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        diff = [(nums1[i]-nums2[i]) for i in range(len(nums1))]
        diff.sort()
        i = 0
        j = len(nums1)-1
        count = 0
        while i < j:
            if diff[i]+diff[j]>0:
                count += j - i
                j -= 1
            else:
                i += 1
        return count