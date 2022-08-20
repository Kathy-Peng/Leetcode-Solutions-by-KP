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
        res = r
        while l <= r:
            mid = l + (r-l+1) // 2
            if self.helper(nums, mid, m):
                res = mid
                r = mid-1
            else:
                l = mid+1
        return res