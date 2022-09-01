class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        last_digit = digits[-1]
        new_digit = (last_digit+1) % 10
        digits[-1]=new_digit
        carry = (last_digit+1)//10
        idx = len(digits)-2
        while idx >=0:
            digit = digits[idx]
            new_digit = (digit+carry)%10
            carry = (digit+carry)//10
            digits[idx]=new_digit
            idx -=1
        if carry!=0:
            digits.insert(0,carry)
            return digits 
        return digits