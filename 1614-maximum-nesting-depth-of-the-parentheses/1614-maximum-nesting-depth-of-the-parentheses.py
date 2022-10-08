class Solution:   
    def maxDepth(self, s: str) -> int:
        stack = []
        max_depth = 0
        for item in s:
            if item == '(':
                stack.append(item)
            elif item == ')':
                if max_depth < len(stack):
                    max_depth = len(stack)
                stack.pop() 
        return max_depth
                
            