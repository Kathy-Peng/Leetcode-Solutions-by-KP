class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        ret_val = 0
        power = 31
        while n!=0:
            bit = n % 2
            if bit:
                ret_val += 2 ** power
            n = n >> 1
            power -= 1
            
        return ret_val
            