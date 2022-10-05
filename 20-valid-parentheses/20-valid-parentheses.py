class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        parentheses = {'(':')', '{':'}', '[':']'}
        for item in s:
            if item in parentheses.keys():
                stack.append(item)
            if item in parentheses.values():
                if len(stack)==0:
                    return False
                openP = stack[-1]
                if parentheses[openP]==item:
                    stack.pop()
                else:
                    return False
        return True if len(stack)==0 else False
            
                