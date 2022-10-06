class Solution(object):
    def removeDuplicates(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        stack = [['$', 0]]
        for item in s:
            if item == stack[-1][0]:
                stack[-1][1] += 1
                if stack[-1][1]==k:
                    stack.pop()
            else:
                stack.append([item, 1])
        ret_string = ''
        for pair in stack:
            ret_string = ret_string + ''.join(pair[0]*pair[1])
        return ret_string
                    
                    
                    