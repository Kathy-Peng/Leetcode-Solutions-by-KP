class Solution(object):
    def helper(self, nums, mid, m):
        subarray = 0
        currSum = 0
        for num in nums:
            currSum += num
            if currSum > mid:
                subarray +=1
                currSum = num
        return subarray+1 <= m
        
    def splitArray(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        """
        l,  r = max(nums), sum(nums)
        while l < r:
            mid = (l + r) // 2
            if self.helper(nums, mid, m):
                r = mid
            else:
                l = mid+1
        return r