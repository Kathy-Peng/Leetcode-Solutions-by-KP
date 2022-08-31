class Solution:
    def isHappy(self, n: int) -> bool:
        prev_list = []
        while True:
            print(prev_list)
            if n == 1:
                return True
            digits = []
            while n // 10 != 0:
                digits.append(n % 10)
                n = n // 10
            digits.append(n % 10)
            
            #reset n here to the next number
            n = 0
            for digit in digits:
                n += digit ** 2
            if n in prev_list:
                return False
            prev_list.append(n)
        
            