class Solution(object):
    def helper(self,sweetness, mid, k):
        substring = 0
        currSum = 0
        for item in sweetness:
            currSum += item
            if currSum >= mid:
                substring += 1
                currSum = 0
        return substring >= k + 1
            
    def maximizeSweetness(self, sweetness, k):
        """
        :type sweetness: List[int]
        :type k: int
        :rtype: int
        """
        l = min(sweetness)
        r = sum(sweetness)
        while l < r:
            mid = l + (r-l+1) / 2
            if self.helper(sweetness, mid, k):
                l = mid 
            else:
                r = mid - 1
        return l