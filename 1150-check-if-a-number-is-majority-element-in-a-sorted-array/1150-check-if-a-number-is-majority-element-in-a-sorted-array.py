class Solution(object):
    def isMajorityElement(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        mid = (len(nums)-1)/2
        if nums[mid]!=target:
            return False
        l = mid
        r = mid
        while l-1>=0 and nums[l-1]==target:
            l -= 1
        while r+1<len(nums) and nums[r+1]==target:
            r += 1
        major = r - l + 1
        return major > len(nums) / 2
            
            
        