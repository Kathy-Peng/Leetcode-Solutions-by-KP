class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        #Explain: we iterate through the array of nums and calculate the needed number comp that can help us reach the target. If this needed number is already present in the hashmap we can return the two indices. Else we can add the number as key and its index as value. This process guarantees that a number won't find itself as the comp needed. 
        hashmap = {}
        for i in range(len(nums)):
            comp = target - nums[i]
            if comp in hashmap:
                return [hashmap[comp], i]
            else:
                hashmap[nums[i]] = i
        print(hashmap)
                
            