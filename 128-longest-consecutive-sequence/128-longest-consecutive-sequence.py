class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        pyset = set()
        pyset.update(nums)
        maxcount = 0
        for item in pyset:
            if item-1 in pyset:
                continue
            else:
                curritem = item
                count = 1
                while curritem+1 in pyset:
                    curritem = curritem+1
                    count+=1
                if count > maxcount:
                    maxcount = count
        return maxcount