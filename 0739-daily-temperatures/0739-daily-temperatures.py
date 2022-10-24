class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = []
        stack = []
        for i in range(len(temperatures)-1, -1, -1):
            while len(stack)!=0 and temperatures[stack[-1]]<=temperatures[i]:
                stack.pop()
            if len(stack)==0:
                answer.append(0)
            else:
                answer.append(stack[-1]-i)
            stack.append(i)
        answer = reversed(answer)
        return answer
            