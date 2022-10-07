class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        wordSet = set(wordDict)
        cache = {}
        
        def helper(sub):
            if sub in cache:
                return cache[sub]
            result = []
            for i in range(len(sub)):
                prefix = sub[:i+1]
                if prefix in wordSet:
                    if prefix == sub:
                        result.append(prefix)
                    else:
                        rest = sub[i+1:]
                        restresult = helper(rest)
                        for item in restresult:
                            result.append(prefix+' '+item)
            cache[sub]=result
            return result
            
        return helper(s)
        