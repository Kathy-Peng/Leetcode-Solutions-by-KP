class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs)==1:
            return strs[0]
        first_string=strs[0]
        for i in range(0,len(first_string)):
            char = first_string[i]
            for j in range(1,len(strs)):
                string = strs[j] 
                if i==len(string) or string[i]!=char:
                    return first_string[:i]
        return first_string
        