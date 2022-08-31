class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = 0
        roman_dict = {'I': 1, 'V':5, 'X': 10, 'L': 50, 'C':100, 'D':500, 'M':1000}
        for i in range(len(s)):
            if i+1 ==len(s) or roman_dict[s[i]]>=roman_dict[s[i+1]]:
                result += roman_dict[s[i]]
            else:
                result -= roman_dict[s[i]]
        return result