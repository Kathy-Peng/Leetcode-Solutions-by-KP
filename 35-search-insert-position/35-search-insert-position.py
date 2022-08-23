class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l = 0
        r = len(nums)-1
        while l < r - 1 : #terminates when l and r are next to each other
            mid = (l+r)/2
            if nums[mid]==target:
                return mid
            elif nums[mid]>target:
                r = mid  
            else:
                l = mid
        if target > nums[r]:
            return r + 1
        if target < nums[l]:
            return l
        if target > nums[l] and target < nums[r]:
            return l + 1
        if target==nums[l]:
            return l
        if target==nums[r]:
            return r