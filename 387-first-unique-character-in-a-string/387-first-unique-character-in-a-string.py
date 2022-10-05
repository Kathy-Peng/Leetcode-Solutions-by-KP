class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        maps = {}
        for item in s:
            if item not in maps:
                maps[item]=1
            else:
                count = maps[item]
                maps[item]=count+1
        for i in range(len(s)):
            if maps[s[i]]==1:
                return i
        return -1
        