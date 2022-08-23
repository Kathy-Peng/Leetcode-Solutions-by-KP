class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_map = {}
        t_map = {}
        for i in range(len(s)):
            if s[i] not in s_map and t[i] not in t_map:
                s_map[s[i]]=t[i]
                t_map[t[i]]=s[i]
            elif s[i] in s_map and t[i] in t_map:
                if t[i]!=s_map[s[i]] or s[i]!= t_map[t[i]]:
                    return False
            else:
                return False
        return True
        
                