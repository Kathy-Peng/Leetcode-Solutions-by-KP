class Solution(object):
    def twoSumLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        l = 0
        r = len(nums)-1
        max_sum = 0
        while l < r:
            currSum = nums[l]+nums[r]
            if currSum<k:
                if max_sum < currSum:
                    max_sum = currSum
                l += 1
            else:
                r -= 1
        return max_sum if max_sum else -1
                
                