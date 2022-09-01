class Solution(object):
    def maxLength(self, ribbons, k):
        """
        :type ribbons: List[int]
        :type k: int
        :rtype: int
        """
        def helper(ribbons, mid, k ):
            return sum([item // mid for item in ribbons]) >= k
       
        l = 0
        r = max(ribbons)
        
        while l < r:
            mid = ( l + r + 1) / 2
            if helper(ribbons, mid, k):
                l = mid
            else:
                r = mid - 1
        return l