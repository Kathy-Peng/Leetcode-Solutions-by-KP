class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_map = collections.defaultdict(int)
        t_map = collections.defaultdict(int)
        for char in s:
            s_map[char] += 1
        for char in t:
            t_map[char] += 1
        if len(s_map)!=len(t_map):
            return False
        for item in s_map:
            if item not in t_map:
                return False
            if s_map[item]!=t_map[item]:
                return False
        return True