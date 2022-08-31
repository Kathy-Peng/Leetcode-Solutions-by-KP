class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        #edge case:
        if len(needle) == 0:
            return 0
        h = 0
        while h < len(haystack):
            if haystack[h]!=needle[0]:
                h +=1
            else:
                if haystack[h:h+len(needle)]==needle:
                    return h
                else:
                    h += 1
        return -1
    
            
                
                