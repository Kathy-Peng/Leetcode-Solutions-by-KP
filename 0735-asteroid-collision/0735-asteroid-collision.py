class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stk = []
        for i in range(len(asteroids)):
            if asteroids[i] > 0:
                stk.append(asteroids[i])
            else:
                while len(stk)!=0 and stk[-1]>0 and abs(stk[-1])<abs(asteroids[i]):
                    stk.pop()
                if len(stk)!=0 and stk[-1]== -asteroids[i]:
                    stk.pop()
                elif len(stk)==0 or stk[-1] < 0 :
                    stk.append(asteroids[i])    
        return stk
                    