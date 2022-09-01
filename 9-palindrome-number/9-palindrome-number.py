class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x = str(x)
        num = len(x) // 2
        return_bool = True
        for i in range(num):
            if x[i]!= x[-1-i]:
                return_bool = False
        return return_bool