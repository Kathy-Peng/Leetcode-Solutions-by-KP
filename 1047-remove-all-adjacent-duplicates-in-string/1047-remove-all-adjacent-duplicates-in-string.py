class Solution(object):
    def removeDuplicates(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        for item in s:
            if len(stack)==0:
                stack.append(item)
            else:
                if stack[-1]==item:
                    stack.pop()
                else:
                    stack.append(item)
        return "".join(stack)
                