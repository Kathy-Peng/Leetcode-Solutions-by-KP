class Solution(object):
    def helper(self, weights, mid, days):
        substring = 1
        currSum = 0
        for item in weights:
            if currSum + item > mid:
                substring += 1
                currSum = item
            else:
                currSum += item
        return substring <= days
    
    def shipWithinDays(self, weights, days):
        """
        :type weights: List[int]
        :type days: int
        :rtype: int
        """
        l = max(weights)
        r = sum(weights)
        while l < r:
            mid = (l + r) / 2
            if self.helper(weights, mid, days):
                r = mid
            else:
                l = mid + 1
        return l