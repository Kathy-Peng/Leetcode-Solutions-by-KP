class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l = 0
        r = len(nums)-1
        while l <= r:
            mid = (l+r)/2
            if nums[mid]==target:
                return mid
            if nums[mid]>target:
                r = mid - 1
            if nums[mid]<target:
                l = mid + 1
        return -1