class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = []
        stack = []
        #step 1: traverse the stack backwards
        for i in range(len(temperatures)-1, -1, -1):
            #step 2: keep popping elements from stack until it's empty or the top of stack is larger than the current element
            while len(stack)!=0 and temperatures[stack[-1]]<=temperatures[i]:
                stack.pop()
            #step 3: if the stack ends up empty then there are no larger elements
            if len(stack)==0:
                answer.append(0)
            else:
            #step 4: if found a larger element, record the distance between them
                answer.append(stack[-1]-i)
            stack.append(i)
        #step 5: since we traverse backwards, we need to reverse the answer
        answer = reversed(answer)
        return answer
            