class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
         
        j = 0 #processed array pointer
        for num in nums:
            #iterate the general array and if a number is not present in the processed array, we add this number to the processed array
            if num != nums[j]:
                j+=1
                nums[j]=num
        return j+1
        