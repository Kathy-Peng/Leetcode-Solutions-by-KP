class Solution(object):
    
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        res = []
        nums.sort()
        ls = len(nums)
        for i, x in enumerate(nums):
            if i > 0 and x == nums[i-1]:
                continue
            l, r = i + 1, ls - 1
            while l < r:
                if nums[l] + nums[r] == -x:
                    res.append([x, nums[l],nums[r]])
                    l += 1
                    while l<r and nums[l]==nums[l-1]:
                        l += 1
                    r -= 1
                    while r > l and nums[r]==nums[r+1]:
                        r -= 1
                elif nums[l]+nums[r] < -x:
                    l += 1
                else:
                    r -= 1
        return res
            
                    