import math
class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        #we cannot use + or - operators but we can use * and **
        n = (2**a) * (2**b)
        return int(math.log(n,2))
        
        