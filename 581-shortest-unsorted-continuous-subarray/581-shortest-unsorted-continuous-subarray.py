class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        j = len(nums)-1
        while i<len(nums)-1:
            if nums[i]<=nums[i+1]:
                i+=1
            else:
                break
        while j>0:
            if nums[j]>=nums[j-1]:
                j-=1
            else:
                break
        if i==j:
            return 0
        
        unordered_subarray = nums[i:j+1]
        if len(unordered_subarray)==0:
            return 0
        else:
            local_min = min(nums[i:j+1])
            local_max = max(nums[i:j+1])
            while i>0 and nums[i-1]>local_min:
                i-=1
            while j<len(nums)-1 and nums[j+1]<local_max:
                j+=1
                
        return j-i+1
