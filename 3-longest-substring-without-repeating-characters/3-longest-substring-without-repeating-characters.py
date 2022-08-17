class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        subsequence = {}
        i= 0
        count = 0
        maxlength = 0
        while i<len(s):
            if s[i] not in subsequence:
                subsequence[s[i]]=i
                count +=1
                i+=1
            else:
                if count > maxlength:
                    maxlength = count
                i = subsequence[s[i]]+1
                count = 0
                subsequence={}
        if count> maxlength:
            maxlength=count
        return maxlength
                