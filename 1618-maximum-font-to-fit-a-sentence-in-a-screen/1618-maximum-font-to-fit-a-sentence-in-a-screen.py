# """
# This is FontInfo's API interface.
# You should not implement it, or speculate about its implementation
# """
#class FontInfo(object):
#    Return the width of char ch when fontSize is used.
#    def getWidth(self, fontSize, ch):
#        """
#        :type fontSize: int
#        :type ch: char
#        :rtype int
#        """
# 
#    def getHeight(self, fontSize):
#        """
#        :type fontSize: int
#        :rtype int
#        """
class Solution(object):
    def maxFont(self, text, w, h, fonts, fontInfo):
        """
        :type text: str
        :type w: int
        :type h: int
        :type fonts: List[int]
        :type fontInfo: FontInfo
        :rtype: int
        """
        
        def helper(font):
            sumWidth = 0
            sumHeight = fontInfo.getHeight(font)
            for char in text:
                sumWidth += fontInfo.getWidth(font, char)
            return sumWidth <= w and sumHeight <= h
        
        l = 0
        r = len(fonts)-1
        while l < r:
            mid = (l + r + 1) /2
            if helper(fonts[mid]):
                l = mid
            else:
                r = mid - 1
        if l == 0:
            if not helper(fonts[l]):
                return -1
        return fonts[l]
            
        
                
            