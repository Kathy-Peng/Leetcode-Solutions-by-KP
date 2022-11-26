class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        result = ''
        stack = []
        for char in s:
            if char !='(' and char !=')':
                result = result + char
            else:
                if char == '(':
                    stack.append(char)
                    result = result + char
                else:
                    if len(stack)!=0 and stack[-1]=='(':
                        stack.pop()
                        result = result + char
        if len(stack)!=0:
            final_result = ''
            count = len(stack)
            for i in range(len(result)-1,-1,-1):
                char = result[i]
                if count !=0 and char == '(':
                    count -= 1
                    continue
                final_result = char + final_result
            result = final_result
        return result     
                    
                    