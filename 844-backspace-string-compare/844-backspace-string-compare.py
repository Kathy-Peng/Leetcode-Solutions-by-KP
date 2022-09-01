class Solution:
    def helper(self, string: str)->str:
        new_string = []
        for i in range(len(string)):
            if string[i]!='#':
                new_string.append(string[i])
            elif len(new_string)!=0:
                new_string.pop()
        return ''.join(new_string)
        
    def backspaceCompare(self, s: str, t: str) -> bool:
        #mimic keystroke from user input:
        s = self.helper(s)
        t = self.helper(t)
        return s==t
        
