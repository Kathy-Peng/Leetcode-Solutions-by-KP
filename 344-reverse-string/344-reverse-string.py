class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        length = len(s)
        left = 0
        right = length -1 
        while left <= right:
            left_tmp = s[left]
            s[left] = s[right]
            s[right] = left_tmp
            left +=1
            right-=1
        return s
    
            