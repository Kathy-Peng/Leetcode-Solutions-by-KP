class Solution(object):
    def count(self, nums, mid):
        '''
        counts the number of missing number in nums up until number k, including number k as well
        '''
        
        count = 0
        for item in nums:
            if item <= mid:
                count += 1
        return mid - nums[0] + 1 - count
            
    def missingElement(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        l = 1
        r = nums[-1]+k
        while l < r:
            mid = (l + r) / 2
            curr = self.count(nums, mid)
            print(mid,curr)
            if curr < k:
                l = mid + 1
            if curr >= k:
                r = mid
        return l 
        