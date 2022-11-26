class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if s1==s2:
            return True
        diff = []
        for i in range(len(s1)):
            if s1[i]!=s2[i]:
                diff.append(i)
        if len(diff)!=2:
            return False
        #swap s1:
        s1 = list(s1)
        tmp = s1[diff[0]]
        s1[diff[0]]=s1[diff[1]]
        s1[diff[1]]=tmp
        s1 = ''.join(s1)
        return s1==s2
        