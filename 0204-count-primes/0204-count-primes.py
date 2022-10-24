class Solution:          
    def countPrimes(self, n: int) -> int:
        if n<3: return 0
        seive = [1 for s in range(n)]
        seive[0] = 0
        seive[1] = 0 
        #step 2: update all composites which are multiples of prime up to number
        i = 2
        while(i*i < n):
            if seive[i]:
                for idx in range(i*i, n, i):
                    seive[idx] = 0
            i += 1 
        return sum(seive)
    
   
        