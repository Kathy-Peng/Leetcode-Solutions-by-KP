class Solution(object):
    def maxLength(self, ribbons, k):
        """
        :type ribbons: List[int]
        :type k: int
        :rtype: int
        """
        def helper(ribbons, mid, k ):
            num = 0
            for item in ribbons:
                num += item // mid
            return num >= k
       
        l = 0
        r = max(ribbons)
        
        while l < r:
            mid = ( l + r + 1) / 2
            if helper(ribbons, mid, k):
                l = mid
            else:
                r = mid - 1
        return l