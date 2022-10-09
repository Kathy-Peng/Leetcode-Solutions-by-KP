class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        max_length = 0
        result = []
        for i in range(len(s)):
            l, r = i, i
            while l >= 0 and r < len(s) and s[l]==s[r]:
                if r-l+1 > max_length:
                    max_length = r-l+1
                    result=[l, r+1]
                l -= 1
                r += 1
        for j in range(len(s)):
            l, r = j, j+1
            while l>=0 and r<len(s) and s[l]==s[r]:
                if r-l+1 > max_length:
                    max_length = r-l+1
                    result = [l, r+1]
                l -= 1
                r += 1
                    
        return s[result[0]:result[1]]
                