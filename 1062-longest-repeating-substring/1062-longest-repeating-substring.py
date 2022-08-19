class Solution(object):
    def repeat(self,s, l):
        '''
        helper function to check if any substring of length l
        occured more than once in the string s
        uses a hashset to store all possible substrings 
        and check if any of them occured more than one
        '''             
        seen = set()
        for i in range(0, len(s)-l+1):
            substring = s[i:i+l]
            if substring in seen:
                return True
            seen.add(substring)
        return False
        
    def longestRepeatingSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        '''
        The possible answers to this question range from 0 to n-1
        where 0 means there are no repeating substrings and n-1 
        means this substring of length n-1 occured exactly twice.
        We can perform binary search between this range and use 
        helper function repeat to check for valid answers
        '''
        l = 0
        r = len(s)-1
        while l < r:
            mid = l + (r-l+1) //2 
            if self.repeat(s,mid):
                l = mid
            else:
                r = mid-1
        return r
            
            
            
            
            