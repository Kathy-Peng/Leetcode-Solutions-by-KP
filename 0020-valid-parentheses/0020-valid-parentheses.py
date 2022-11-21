class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        #stores only open parentheses but will be eliminated when encountering a close parentheses
        hashmap = {'(':')', '{':'}', '[':']'}
        for item in s:
            if item in hashmap:
                stk.append(item)
            if item in hashmap.values():
                if len(stk)>0 and hashmap[stk[-1]]==item:
                    stk.pop()
                else:
                    return False
        return len(stk)==0
            