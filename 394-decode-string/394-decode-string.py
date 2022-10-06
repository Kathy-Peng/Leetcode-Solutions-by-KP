class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        #step 1: keep adding chars into the stack until we find a close bracket
        for item in s:
            if item != ']':
                stack.append(item)
        #step 2: after we find a close bracket, pop everything until an open bracket
            else:
                contents = ''
                while stack[-1] !='[':
                    contents = stack.pop() + contents
        #step 3: pop the open bracket and identify the multiples of digits
                stack.pop()
                digits = ''
                while len(stack)!=0 and stack[-1].isnumeric():
                    digits = stack.pop() + digits
                multiple = int(digits)
        #step 4: push to the stack multiples * contents 
                for i in range(multiple):
                    for char in contents:
                        stack.append(char)
        return ''.join(stack)
                